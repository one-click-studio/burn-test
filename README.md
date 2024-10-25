# Burn
Testing inference of Onnx models using the Burn crate.

## Usage
Test the conversion of provided [models](./models/) by setting the `MODEL_FILE` environment variable: 
```sh
MODEL_FILE=head-pose-estimation-adas-0001.onnx cargo build
MODEL_FILE=version-RFB-320.onnx cargo build
MODEL_FILE=version-RFB-640.onnx cargo build
```

## Models sources
**head-pose-estimation-adas-0001** is an [OpenVino](https://docs.openvino.ai/2024/omz_models_model_head_pose_estimation_adas_0001.html) model. It was converted to Onnx using the Python scripts found in [openvino_to_onnx](./openvino_to_onnx/).

**version-RFB-320.onnx** and **version-RFB-640.onnx** are the same model base, with different image input sizes. Coming from the [Ultra-lightweight face detection model](https://github.com/onnx/models/tree/main/validated/vision/body_analysis/ultraface).