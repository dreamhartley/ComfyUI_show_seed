# ComfyUI Show Seed

A ComfyUI custom node that saves images while displaying the seed value used in generation.

## Features

- Saves images with automatic numbering
- Extracts and displays seed value from KSampler nodes
- Preserves workflow data in image metadata

## Installation

### Manual Installation
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/dreamhartley/ComfyUI_show_seed.git
```

## Usage

1. Find the node under the "image" category as "Save Image(show seed)"
2. Connect your image output to this node
3. Set your desired filename prefix
4. The node will save your image and display the seed used in generation

## Example Workflow

![Example Workflow](example/workflow.png)

## License

This project is licensed under the MIT License.
