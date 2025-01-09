import os
import numpy as np
import json
from PIL import Image
from PIL.PngImagePlugin import PngInfo

class ShowSeed:
    def __init__(self):
        self.output_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')
        self.type = "output"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE", ),
                "filename_prefix": ("STRING", {"default": "ComfyUI"}),
            },
            "hidden": {
                "prompt": "PROMPT",
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("seed_info",)
    FUNCTION = "save_images"
    OUTPUT_NODE = True
    CATEGORY = "image"

    def extract_seed(self, prompt):
        try:
            if isinstance(prompt, tuple):
                prompt = prompt[1]
            if isinstance(prompt, dict):
                for node_data in prompt.values():
                    if isinstance(node_data, dict):
                        class_type = node_data.get('class_type', '')
                        if 'KSampler' in class_type:
                            inputs = node_data.get('inputs', {})
                            if 'seed' in inputs:
                                return inputs['seed']
            return None
        except Exception as e:
            print(f"Error extracting seed: {str(e)}")
            return None

    def save_images(self, images, filename_prefix="ComfyUI", prompt=None):
        os.makedirs(self.output_dir, exist_ok=True)
        results = list()
        seed_value = self.extract_seed(prompt)
        seed_text = f"Seed: {seed_value}" if seed_value is not None else "Seed not found"

        for image in images:
            i = 255. * image.cpu().numpy()
            img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
            
            counter = 1
            while True:
                filename = f"{filename_prefix}_{counter:05}_.png"
                save_path = os.path.join(self.output_dir, filename)
                if not os.path.exists(save_path):
                    break
                counter += 1

            metadata = PngInfo()
            if isinstance(prompt, tuple):
                workflow = prompt[1]
            else:
                workflow = prompt

            if workflow is not None:
                metadata.add_text("prompt", json.dumps(workflow))
                metadata.add_text("workflow", json.dumps(workflow))

            img.save(save_path, format='PNG', pnginfo=metadata)
            results.append({
                "filename": filename,
                "path": save_path,
                "type": "output",
            })

        return {"ui": {"images": results}, "result": (seed_text,)}

# Node Mapping
NODE_CLASS_MAPPINGS = {
    "Save Image(show seed)": ShowSeed
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Save Image(show seed)": "Save Image(show seed)"
}