# Burn
Testing inference of Onnx models using the Burn crate.

## Usage
Test the conversion of provided [models](./models/) by setting the `MODEL_FILE` environment variable: 
```sh
MODEL_FILE=head-pose-estimation-adas-0001.onnx cargo build
MODEL_FILE=version-RFB-320.onnx cargo build
MODEL_FILE=version-RFB-640.onnx cargo build
```
