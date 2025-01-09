class ShowSeed:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "images": ("IMAGE",),
            },
            "hidden": {
                "prompt": "PROMPT",
            }
        }

    RETURN_TYPES = ("IMAGE", "STRING",)
    RETURN_NAMES = ("images", "seed_info",)
    FUNCTION = "process"
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

    def process(self, images, prompt=None):
        # 提取seed
        seed_value = self.extract_seed(prompt)
        seed_text = f"Seed: {seed_value}" if seed_value is not None else "Seed not found"
        
        # 直接返回图像和seed信息
        return (images, seed_text)

# 节点映射
NODE_CLASS_MAPPINGS = {
    "Show Seed": ShowSeed
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Show Seed": "Show Seed"
}
