import onnx

onnx_model = onnx.load("alexnet.onnx")
onnx.checker.check_model(onnx_model)
