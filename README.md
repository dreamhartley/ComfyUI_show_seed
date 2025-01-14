# ComfyUI Show Seed

A ComfyUI custom node that extracts and displays the seed value used in image generation, making it easier to track and reuse successful generations.

## Why This Node?

-   ComfyUI randomly updates seed values after each generation
-   Default interface doesn't show seed values intuitively
-   Helps maintain seed consistency when upscaling images

## Features

-   Displays seed values from KSampler nodes in real-time
-   Passes through image data unchanged
-   Simple integration with existing workflows
-   Zero configuration required - just plug and play

## Usage

Connect it after your KSampler node, and the seed value will be displayed directly on the node.

## Installation

### Method 1: Use ComfyUI Manager

This custom node is now included in the ComfyUI Manager.

1. Open ComfyUI Manager.
2. Click on "Install Custom Nodes".
3. Search for "Show Seed".
4. Click "Install" next to the "ComfyUI Show Seed" entry.
5. Restart ComfyUI.

### Method 2: Manual Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/dreamhartley/ComfyUI_show_seed.git
```

## Example Workflow

![Example Workflow](example/workflow.png)

The node works as a pass-through for image data while extracting the seed information:

-   Input image → Show Seed → Save Image node
-   Show Seed (seed_info) → Text node

## Node Outputs

-   **images**: Original image data (connect to Save Image node)
-   **seed_info**: Extracted seed value (connect to Text node)

## License

This project is licensed under the MIT License.
