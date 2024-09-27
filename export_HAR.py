from hailo_sdk_client import ClientRunner

chosen_hw_arch = "hailo8l"
onnx_path = f"./{model_name}.onnx"

runner = ClientRunner(hw_arch=chosen_hw_arch)
hn, npz = runner.translate_onnx_model(
		onnx_path,
		onnx_model_name,
)

hailo_model_har_name = f"{model_name}.har"
runner.save_har(hailo_model_har_name)
