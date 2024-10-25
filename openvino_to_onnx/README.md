# Convert OpenVINO IR models to ONNX format
The conversion part is based on [this python project](https://github.com/LoSealL/openvino2onnx).

Microsoft ONNX runtime is only compatible with old ONNX formats, as described [here](https://onnxruntime.ai/docs/reference/compatibility.html).
The runtime 1.17.1 is compatible with opset 20 and IR 9. So the process also requires a setp to adjust the file format.

## Requirements
```py
pip install openvino2onnx
pip install openvino==2023.3.0
pip install torchvision
```

## Instructions
### 1. Convert model
```py
python3 -m openvino2onnx 'face-detection-0200.xml'
```

This will create a `.onnx` file in the folder where the script is executed from.

The script can sometimes generate multiple models that needs to be merge. A script will directly be provided in the console output. Copy and run it if needed.


###  2. Convert IR version
```py
# input, output, version
python3 ir_version_converter.py 'face-detection-0200_composed.onnx'  ./test.onnx --target_ir_version 9
```

## Note
If the opset needs to be converted, a script also exists:
```py
# input, version, output
python3 version_converter.py 'face-detection-0200_composed.onnx 20' ./test.onnx
```