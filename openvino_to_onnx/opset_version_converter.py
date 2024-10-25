# Copyright (c) ONNX Project Contributors

# SPDX-License-Identifier: Apache-2.0
"""onnx version converter

This enables users to convert their models between different opsets within the
default domain ("" or "ai.onnx").
"""
from __future__ import annotations

import argparse
import onnx
import onnx.onnx_cpp2py_export.version_converter as C  # noqa: N812
from onnx import ModelProto


def convert_version(model: ModelProto, target_version: int) -> ModelProto:
    """Convert opset version of the ModelProto.

    Arguments:
        model: Model.
        target_version: Target opset version.

    Returns:
        Converted model.

    Raises:
        RuntimeError when some necessary conversion is not supported.
    """
    if not isinstance(model, ModelProto):
        raise TypeError(
            f"VersionConverter only accepts ModelProto as model, incorrect type: {type(model)}"
        )
    if not isinstance(target_version, int):
        raise TypeError(
            f"VersionConverter only accepts int as target_version, incorrect type: {type(target_version)}"
        )
    model_str = model.SerializeToString()
    converted_model_str = C.convert_version(model_str, target_version)
    return onnx.load_from_string(converted_model_str)


ConvertError = C.ConvertError

def main():
    parser = argparse.ArgumentParser(description="Convert ONNX model to a different opset version.")
    parser.add_argument("model_path", type=str, help="Path to the input ONNX model file.")
    parser.add_argument("target_version", type=int, help="Target opset version to convert the model to.")
    parser.add_argument("output_path", type=str, help="Path to save the converted ONNX model file.")

    args = parser.parse_args()

    model = onnx.load(args.model_path)
    converted_model = convert_version(model, args.target_version)
    onnx.save(converted_model, args.output_path)
    print(f"Model converted to opset version {args.target_version} and saved to {args.output_path}")

if __name__ == "__main__":
    main()

