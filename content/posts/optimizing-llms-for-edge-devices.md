+++
date = '2024-03-19T09:00:00-07:00'
draft = false
title = 'Optimizing LLMs for Edge Devices: A GCP & Hugging Face Tutorial'
description = 'A comprehensive guide on using Google Cloud Platform and Hugging Face Transformers to optimize Large Language Models for edge devices through techniques like distillation, quantization, and pruning.'
tags = ['AI', 'Machine Learning', 'Edge Computing', 'GCP', 'Hugging Face']
categories = ['Tutorials']
+++

This tutorial provides a guide on using Google Cloud Platform (GCP) and Hugging Face Transformers to fine-tune a small Large Language Model (LLM), and then apply techniques like distillation, quantization, and pruning to make it suitable for resource-constrained environments such as mobile phones and web browsers (via JavaScript).

1\. Introduction to Google Cloud Platform (GCP)
-----------------------------------------------

**What is GCP?** Google Cloud Platform is a suite of cloud computing services offered by Google. It provides a wide array of services in areas like computing, storage, databases, networking, machine learning, and more, running on the same infrastructure that Google uses to run its end-user products (like Google Search, Gmail, and YouTube).

**Key GCP Services for ML:** For this workflow, the following GCP services are particularly relevant:

-   **Vertex AI:** A unified MLOps platform to build, deploy, and manage ML models.

    -   **Vertex AI Workbench:** Jupyter notebook-based development environment for ML.

    -   **Vertex AI Training:** For running custom training jobs at scale, with support for GPUs and TPUs.

    -   **Vertex AI Prediction:** For deploying models and serving predictions.

-   **Compute Engine:** Provides virtual machines (VMs) that can be configured with various CPU, GPU, and memory options. Useful for development and custom training setups.

-   **Cloud Storage:** Scalable and durable object storage for your datasets, model checkpoints, and other artifacts.

-   **Artifact Registry:** A service to store and manage container images and language packages (like Docker images for your training environment).

**Why use GCP for this workflow?**

-   **Scalability:** Easily scale your compute resources up or down based on the demands of training and experimentation.

-   **Specialized Hardware:** Access to powerful GPUs (NVIDIA A100, T4, V100) and TPUs, which can significantly accelerate model training.

-   **Managed Services:** Vertex AI simplifies many MLOps tasks, allowing you to focus more on model development.

-   **Integration:** Seamless integration between various GCP services (e.g., loading data from Cloud Storage into a Vertex AI training job).

2\. Setting Up Your Environment on GCP
--------------------------------------

1.  **Create a GCP Project:** If you don't have one, create a new project in the Google Cloud Console.

2.  **Enable APIs:** Ensure that the following APIs are enabled for your project:

    -   Compute Engine API

    -   Vertex AI API

    -   Cloud Storage API

    -   Artifact Registry API

3.  **Set up Authentication & gcloud CLI:**

    -   Install the Google Cloud SDK (which includes the `gcloud` command-line tool).

    -   Authenticate: `gcloud auth login` and `gcloud auth application-default login`.

    -   Configure your project: `gcloud config set project YOUR_PROJECT_ID`.

4.  **Choose your Development Environment:**

    -   **Vertex AI Workbench:**

        -   Navigate to Vertex AI in the Cloud Console.

        -   Go to "Workbench" and create a new "Managed notebooks" or "User-managed notebooks" instance.

        -   Choose an instance type with appropriate CPU, RAM, and optionally a GPU.

        -   Select a suitable environment (e.g., PyTorch, TensorFlow) or customize it.

    -   **Compute Engine VM:**

        -   Navigate to Compute Engine.

        -   Create a new VM instance.

        -   Select a machine type (e.g., `n1-standard-4` or a GPU-enabled instance).

        -   Choose a boot disk image (e.g., "Deep Learning on Linux").

        -   SSH into your VM and install necessary libraries:

            ```
            pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 # Or your specific CUDA version
            pip install transformers[torch] datasets accelerate optimum[onnxruntime,neural-compressor]
            pip install tensorflow # If using TensorFlow
            pip install tensorflow_model_optimization # For TF pruning/quantization
            pip install tf2onnx # For TF to ONNX conversion

            ```

3\. Fine-Tuning a Small LLM with Hugging Face Transformers
----------------------------------------------------------

**Choosing a Small Base Model:** Start with a pre-trained model that is already relatively small. Examples:

-   **BERT-based:** `distilbert-base-uncased`, `google/mobilebert-uncased`, `prajjwal1/bert-tiny`

-   **GPT-2-based:** `gpt2` (the smallest version), or distilled versions if available.

-   **Other architectures:** Models specifically designed for efficiency.

**Preparing Your Dataset:**

-   Your dataset should be formatted appropriately for your task (e.g., text classification, question answering).

-   Use the Hugging Face `datasets` library to load and preprocess your data.

-   Upload your dataset to a Cloud Storage bucket for easy access from your GCP environment.

**The Fine-Tuning Script:** Use the Hugging Face `Trainer` API for a high-level training loop or write a custom PyTorch/TensorFlow training loop.

*Example Conceptual Structure (using `Trainer`):*

```
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer

# 1. Load Tokenizer and Model
model_name = "distilbert-base-uncased" # Or your chosen small model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=NUM_LABELS)

# 2. Load and Preprocess Dataset
# Example: dataset = load_dataset("your_dataset_script.py", data_dir="gs://your-bucket/your-data/")
# Or load from Hugging Face Hub, local files, etc.
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

# tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
# Ensure your dataset has 'labels' column for classification

# 3. Define Training Arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    # For GCP:
    # report_to="wandb", # Optional: for experiment tracking
    # push_to_hub=False, # Or True if you want to save to Hugging Face Hub
)

# 4. Initialize Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"], # or "test"
    tokenizer=tokenizer,
    # data_collator, compute_metrics can be added
)

# 5. Start Fine-Tuning
trainer.train()

# 6. Save the fine-tuned model
trainer.save_model("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")

```

**Leveraging GCP for Training:**

-   **Vertex AI Training:** Package your training script into a Docker container and submit it as a custom training job. This allows you to specify machine types (including GPUs/TPUs) and run training without managing infrastructure directly.

-   **Compute Engine with GPU:** If using a VM, ensure you've selected an instance with a GPU and have the necessary NVIDIA drivers and CUDA toolkit installed. The `accelerate` library from Hugging Face can help simplify distributed training.

4\. Knowledge Distillation
--------------------------

**Concept:** Knowledge distillation is a model compression technique where a smaller "student" model is trained to mimic the behavior of a larger, pre-trained "teacher" model. The student learns from the teacher's soft labels (probabilities for each class) or intermediate representations, in addition to the true labels.

**How it works with Hugging Face:**

-   You'll need a fine-tuned teacher model (can be a larger, more accurate model) and a smaller student model architecture.

-   The loss function is typically a combination of:

    -   Standard cross-entropy loss with the ground truth labels.

    -   A distillation loss (e.g., Kullback-Leibler divergence) between the student's and teacher's output probability distributions.

-   Hugging Face doesn't have a universal `KnowledgeDistillationTrainer` for all tasks, but you can implement it by:

    -   Subclassing the `Trainer` and overriding `compute_loss`.

    -   Writing a custom training loop.

*Example Conceptual `compute_loss` for Distillation (PyTorch):*

```
import torch.nn.functional as F
import torch

# Inside your custom Trainer or training loop:
# teacher_model.eval() # Teacher in eval mode

# def compute_loss(model, inputs, return_outputs=False):
#     labels = inputs.pop("labels")
#     student_outputs = model(**inputs)
#     student_logits = student_outputs.logits

#     # Standard loss with hard labels
#     loss_ce = F.cross_entropy(student_logits, labels)

#     # Distillation loss with soft labels from teacher
#     with torch.no_grad():
#         teacher_outputs = teacher_model(**inputs)
#         teacher_logits = teacher_outputs.logits

#     loss_kd = F.kl_div(
#         input=F.log_softmax(student_logits / temperature, dim=-1),
#         target=F.softmax(teacher_logits / temperature, dim=-1),
#         reduction="batchmean"
#     ) * (temperature ** 2)

#     loss = alpha * loss_ce + (1. - alpha) * loss_kd
#     return (loss, student_outputs) if return_outputs else loss

# `temperature` and `alpha` are hyperparameters for distillation.

```

**Benefits:**

-   Can significantly reduce model size while retaining a good portion of the teacher's performance.

-   Often leads to faster inference.

5\. Quantization
----------------

**Concept:** Quantization involves reducing the numerical precision of the model's weights and/or activations (e.g., from 32-bit floating-point (FP32) to 8-bit integer (INT8) or FP16).

**Benefits:**

-   **Smaller model size:** INT8 models are roughly 4x smaller than FP32.

-   **Faster inference:** Integer operations are often faster on CPUs and specialized hardware (like mobile NPUs).

-   **Reduced power consumption.**

**Tools & Techniques:**

-   **Hugging Face Optimum:** A library that extends `transformers` and provides optimization tools, including quantization through backends like ONNX Runtime and Intel Neural Compressor.

    ```
    pip install optimum[onnxruntime] # or optimum[neural-compressor]

    ```

    *Example Post-Training Dynamic Quantization with Optimum & ONNX Runtime:*

    ```
    from optimum.onnxruntime import ORTQuantizer, ORTModelForSequenceClassification
    from optimum.onnxruntime.configuration import AutoQuantizationConfig

    # Load your fine-tuned (or distilled) PyTorch model
    model_checkpoint = "./fine_tuned_or_distilled_model"
    onnx_model_path = "./onnx_model"
    quantized_model_path = "./quantized_onnx_model"

    # 1. Export to ONNX
    ort_model = ORTModelForSequenceClassification.from_pretrained(model_checkpoint, export=True)
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    ort_model.save_pretrained(onnx_model_path)
    tokenizer.save_pretrained(onnx_model_path) # Save tokenizer with ONNX model

    # 2. Create Quantizer
    quantizer = ORTQuantizer.from_pretrained(onnx_model_path)

    # 3. Define Quantization Config (Dynamic Quantization)
    dqconfig = AutoQuantizationConfig.arm64(is_static=False, per_channel=False) # For mobile
    # Or: dqconfig = AutoQuantizationConfig.avx512_vnni(is_static=False, per_channel=False) # For CPUs

    # 4. Apply Quantization
    quantizer.quantize(save_dir=quantized_model_path, quantization_config=dqconfig)

    ```

-   **Post-Training Static Quantization (PTSQ):** Requires a calibration dataset to determine scaling factors. Generally more accurate than dynamic quantization. Optimum supports this with ONNX Runtime and Neural Compressor.

-   **Quantization-Aware Training (QAT):** Simulates quantization effects during the fine-tuning process. Can lead to better accuracy but is more complex to implement. PyTorch and TensorFlow have QAT utilities.

    -   PyTorch: `torch.quantization` module.

    -   TensorFlow: `tfmot.quantization.keras` (TensorFlow Model Optimization Toolkit).

6\. Pruning
-----------

**Concept:** Pruning involves removing redundant or less important weights, neurons, or even larger structures (like attention heads or layers) from the model.

**Benefits:**

-   **Reduced model size.**

-   **Potentially faster inference** (especially with structured pruning).

**Types & Tools:**

-   **Unstructured Pruning (Weight Pruning):** Individual weights are set to zero. Can lead to sparse models. Requires specialized hardware or libraries for speedup.

-   **Structured Pruning:** Entire neurons, channels, or attention heads are removed. This often results in a smaller, dense model that can run faster on standard hardware.

-   **Hugging Face Optimum:** Can leverage `neural-compressor` for some pruning techniques.

-   **PyTorch:** `torch.nn.utils.prune` module for implementing various pruning techniques (magnitude, L1 unstructured, etc.).

-   **TensorFlow Model Optimization Toolkit (TF MOT):** `tfmot.sparsity.keras` provides tools for pruning during or after training.

*Example Conceptual Pruning (PyTorch - Magnitude Pruning):*

```
import torch.nn.utils.prune as prune

# model = your_fine_tuned_model
# parameters_to_prune = (
#     (model.bert.encoder.layer[0].attention.self.query, 'weight'),
#     (model.bert.encoder.layer[0].output.dense, 'weight'),
#     # ... add more layers and parameters
# )

# prune.global_unstructured(
#     parameters_to_prune,
#     pruning_method=prune.L1Unstructured,
#     amount=0.3,  # Prune 30% of the weights with the smallest L1 norm
# )

# # To make pruning permanent and remove zeroed weights (if supported by subsequent steps)
# for module, param_name in parameters_to_prune:
#   prune.remove(module, param_name)

```

After pruning, the model usually needs to be fine-tuned again for a few epochs ("iterative pruning") to recover any lost accuracy.

7\. Exporting and Running on Client Devices
-------------------------------------------

After applying these optimization techniques, you need to export the model to a format suitable for client-side inference.

**Common Formats:**

-   **ONNX (Open Neural Network Exchange):** An open format for ML models. Widely supported and can be run with ONNX Runtime.

-   **TensorFlow Lite (TFLite):** Optimized for mobile and edge devices. Offers good performance and small binary size.

**A. For In-Browser (JavaScript):**

1.  **ONNX Runtime Web:**

    -   Convert your Pytorch/TF model to ONNX (as shown in quantization section).

    -   The quantized ONNX model is ideal here.

    -   Use `onnxruntime-web` library in your JavaScript project.

    ```
    <script src="https://cdn.jsdelivr.net/npm/onnxruntime-web/dist/ort.min.js"></script>

    ```

    ```
    // async function runInference(modelPath, inputData) {
    //   try {
    //     const session = await ort.InferenceSession.create(modelPath);
    //     const feeds = { /* ... prepare your input tensor(s) ... */ };
    //     const results = await session.run(feeds);
    //     // Process results
    //     console.log(results);
    //   } catch (e) {
    //     console.error(`Failed to run inference: ${e}`);
    //   }
    // }
    // runInference('./quantized_onnx_model/model.onnx', /* your input */);

    ```

    -   Input preparation (tokenization) needs to be replicated in JavaScript. You can use a JS tokenizer compatible with your Hugging Face tokenizer or implement it. Libraries like `tokenizers.js` (from Hugging Face) or simpler custom tokenizers can be used.

2.  **TensorFlow.js (TFJS):**

    -   Convert your TensorFlow model to TFJS format, or TFLite model to TFJS.

    -   Use the `tfjs-tflite` package to run TFLite models.

    ```
    pip install tensorflowjs
    tensorflowjs_converter --input_format=tf_lite --output_format=tfjs_graph_model ./model.tflite ./tfjs_model

    ```

    ```
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/universal-sentence-encoder@latest/dist/universal-sentence-encoder.min.js"></script> <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs-tflite@latest/dist/tf-tflite.min.js"></script>

    ```

    ```
    // async function runTFLiteInBrowser(modelPath) {
    //   const tfliteModel = await tflite.loadTFLiteModel(modelPath);
    //   // const inputTensor = tf.tensor(...); // Prepare input
    //   // const outputTensor = tfliteModel.predict(inputTensor);
    //   // console.log(outputTensor.dataSync());
    // }

    ```

3.  **Transformers.js (by Xenova/Hugging Face):**

    -   This library allows you to run many Hugging Face Transformers models directly in the browser. It handles model conversion (to ONNX) and tokenization automatically for supported models.

    -   It's the easiest way if your model architecture and tokenizer are supported.

    ```
    <script type="module">
      import { pipeline, AutoTokenizer, AutoModelForSequenceClassification } from '@xenova/transformers';
      // For locally converted/optimized models:
      // const classifier = await pipeline('text-classification', './path_to_your_quantized_onnx_model_directory/');
      // const output = await classifier('I love transformers!');
      // console.log(output);

      // Or load a pre-quantized model from Hub if available
      // let tokenizer = await AutoTokenizer.from_pretrained('Xenova/distilbert-base-uncased-finetuned-sst-2-english');
      // let model = await AutoModelForSequenceClassification.from_pretrained('Xenova/distilbert-base-uncased-finetuned-sst-2-english', { quantized: true });
    </script>

    ```

**B. For Mobile Phones (Android/iOS):**

1.  **TensorFlow Lite (TFLite):**

    -   Convert your model (PyTorch/TF -> ONNX -> TFLite or TF -> TFLite).

        ```
        # If starting from ONNX (e.g., after Optimum quantization)
        pip install onnx-tf
        onnx-tf convert -i model.onnx -o model_tf_saved_model

        # Then convert SavedModel to TFLite
        converter = tf.lite.TFLiteConverter.from_saved_model("./model_tf_saved_model")
        converter.optimizations = [tf.lite.Optimize.DEFAULT] # Applies PTQ (dynamic range or int8)
        # For FP16 quantization:
        # converter.target_spec.supported_types = [tf.float16]
        tflite_model = converter.convert()
        with open("model.tflite", "wb") as f:
            f.write(tflite_model)

        ```

    -   Integrate the `.tflite` model into your Android (Java/Kotlin) or iOS (Swift/Objective-C) app using the TensorFlow Lite SDK.

    -   Handle tokenization natively or use pre-built libraries.

2.  **ONNX Runtime Mobile:**

    -   Use the quantized ONNX model.

    -   ONNX Runtime has prebuilt packages for Android and iOS.

    -   Supports various hardware accelerators (NNAPI for Android, Core ML for iOS).

3.  **Core ML (iOS):**

    -   Convert your model to Core ML format using `coremltools`.

    -   Integrate into your iOS app.

**Considerations for Client-Side Deployment:**

-   **Tokenization:** This is a critical step. The exact same tokenization logic used during training must be replicated on the client. This can be challenging in JavaScript or mobile native code.

    -   Consider using sentencepiece or byte-pair encoding (BPE) tokenizers that have JavaScript/native implementations.

    -   Hugging Face `tokenizers` library has Rust core, with bindings for Node.js, and can be compiled to WASM for browser.

-   **Model Size:** Even after optimization, ensure the model is small enough for reasonable download times and memory usage.

-   **Inference Speed:** Test on target devices.

-   **UI/UX:** Provide feedback to the user during model loading and inference.

8\. Workflow Summary and Best Practices
---------------------------------------

The process is often iterative:

1.  **Baseline:** Fine-tune a small LLM on GCP. Evaluate its performance and size.

2.  **Distill (Optional but Recommended):** If you have a larger, more accurate teacher model, distill knowledge into your smaller student model. Evaluate.

3.  **Prune (Optional):** Apply pruning techniques. Evaluate. May require some retraining.

4.  **Quantize:** Apply post-training quantization (dynamic or static) or QAT. Evaluate accuracy and performance. This is often the most impactful step for size and speed on edge devices.

5.  **Export:** Convert to ONNX, TFLite, or other suitable formats.

6.  **Test on Target:** Thoroughly test on target browsers/devices for functionality, speed, and memory usage.

**Best Practices:**

-   **Evaluate at Each Step:** Measure accuracy, model size, and ideally inference speed after each optimization technique. There's usually a trade-off.

-   **Start Simple:** Begin with simpler techniques like dynamic quantization before moving to more complex ones like QAT or extensive pruning.

-   **Calibration Data:** For static quantization, use a representative calibration dataset.

-   **Hardware Awareness:** The best quantization/export format might depend on the target hardware (e.g., specific mobile SoCs, browser WASM capabilities).

-   **Iterate:** Don't expect perfection on the first try. Optimization is an iterative process of tweaking and re-evaluating.

This tutorial provides a high-level roadmap. Each step involves detailed considerations and code. Refer to the official documentation of Hugging Face (Transformers, Optimum, Tokenizers), PyTorch, TensorFlow, ONNX Runtime, and GCP for specific implementation details.