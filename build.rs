use burn_import::onnx::ModelGen;
use std::env;
use std::path::Path;

fn main() {
    let models_dir = "models/";
    
    let file_name = match env::var("MODEL_FILE") {
        Ok(val) => val,
        Err(_) => {
            eprintln!("Error: The environment variable MODEL_FILE is not set.");
            std::process::exit(1);
        }
    };

    let model_path = Path::new(models_dir).join(file_name);

    if !model_path.exists() {
        eprintln!("Error: The specified file does not exist: {:?}", model_path);
        std::process::exit(1);
    }

    if model_path.extension().and_then(|ext| ext.to_str()) != Some("onnx") {
        eprintln!("Error: The specified file is not an ONNX file: {:?}", model_path);
        std::process::exit(1);
    }

    println!("Processing file: {:?}", model_path);
    ModelGen::new()
        .input(model_path.to_str().unwrap())
        .out_dir("models/")
        .run_from_script();
}
