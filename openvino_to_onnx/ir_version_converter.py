import onnx
import argparse

def convert_ir_version(input_model_path, output_model_path, target_ir_version):
    # Load the existing ONNX model
    model = onnx.load(input_model_path)

    # Display the original IR version
    print(f"Original IR version: {model.ir_version}")

    # Change the IR version to the target version
    model.ir_version = target_ir_version

    # Save the updated model
    onnx.save(model, output_model_path)

    print(f"Updated model saved with IR version {model.ir_version} to {output_model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert the IR version of an ONNX model.")
    parser.add_argument("input_model_path", type=str, help="Path to the input ONNX model")
    parser.add_argument("output_model_path", type=str, help="Path to save the converted ONNX model")
    parser.add_argument("--target_ir_version", type=int, default=9, help="Target IR version (default is 9)")

    args = parser.parse_args()

    convert_ir_version(args.input_model_path, args.output_model_path, args.target_ir_version)

