# ResNet18 Inference on Hailo Device

This repository provides example code to run the ResNet18 model on a Hailo device. The example demonstrates how to convert a model to the Hailo Executable File (HEF) format and then perform inference using the Hailo SDK.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Generate the HEF File](#step-1-generate-the-hef-file)
  - [Step 2: Run Inference on the Hailo Device](#step-2-run-inference-on-the-hailo-device)
- [Code Overview](#code-overview)
  - [`make_hef.py`](#make_hefpy)
  - [`run_hailo.py`](#run_hailopy)
- [Notes](#notes)

## Prerequisites

- **Python** 3.6 or higher
- **Hailo SDK** installed and configured
- **Hailo device** connected and operational
- **Python packages**:
  - `numpy`
  - `queue`
  - `threading`
  - `functools`

**Note**: Ensure that you have the Hailo SDK installed and properly configured on your system. Refer to the [Hailo SDK documentation](https://docs.hailo.ai/) for installation instructions.

## Installation

**Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/your-repository.git
```
**Navigate to the project directory:**
```bash
cd your-repository
```
**Install the required Python packages:**

```bash
pip install -r requirements.txt
```

## Usage
**Step 1: Generate the HEF File**
First, run the make_hef.py script to generate the HEF file. This script exports the ONNX model, creates a Hailo Application Representation (HAR), and compiles it into a Hailo Executable File (HEF). The example uses the ResNet18 model.

```bash
python make_hef.py
```
**Step 2: Run Inference on the Hailo Device**
Next, use the run_hailo.py script to perform inference using the HEF file generated in the previous step.

```bash
python run_hailo.py
```
Code Overview
make_hef.py
Purpose: Converts the ResNet18 model into a format suitable for execution on the Hailo device.
Processes:
Exports the model to ONNX format.
Creates a Hailo Application Representation (HAR) file.
Compiles the HAR into a Hailo Executable File (HEF).
run_hailo.py
- Purpose: Runs inference using the HEF file on the Hailo device.
- Processes:
Initializes the Hailo device and loads the HEF file.
Prepares input data and queues for asynchronous processing.
Performs inference and processes the output results.

## Notes
- Device Connection: Ensure that the Hailo device is properly connected and recognized by your system before running the scripts.
- Batch Size: The default batch size is set to 8. You can modify it in the main() function of the scripts.
- Input Data: The example uses randomly generated data. Replace it with actual image data as needed.
