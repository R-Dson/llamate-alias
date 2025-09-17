# Model Aliases for llamate

This file lists available model aliases and their default arguments.

You can add these models to your `llamate` setup using the commands shown.

## [magistral:small-2509](https://huggingface.co/unsloth/Magistral-Small-2509-GGUF)
```bash
llamate add magistral:small-2509
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.7"
- top-p: "0.95"
- jinja: ""
- flash-attn: "on"

</details>

## [ernie-4.5:21b](https://huggingface.co/bartowski/baidu_ERNIE-4.5-21B-A3B-Thinking-GGUF)
```bash
llamate add ernie-4.5:21b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.3"
- jinja: ""
- flash-attn: "on"

</details>

## [nemotron-nano:9b](https://huggingface.co/bartowski/nvidia_NVIDIA-Nemotron-Nano-9B-v2-GGUF)
```bash
llamate add nemotron-nano:9b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- jinja: ""
- flash-attn: "on"

</details>

## [nemotron-nano:12b](https://huggingface.co/bartowski/nvidia_NVIDIA-Nemotron-Nano-12B-v2-GGUF)
```bash
llamate add nemotron-nano:12b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- jinja: ""
- flash-attn: "on"

</details>

## [gpt-oss:120b](https://huggingface.co/ggml-org/gpt-oss-120b-GGUF)
```bash
llamate add gpt-oss:120b
```
<details> <summary>parameters</summary>

- ctx-size: "16384"
- temp: "1.0"
- top-p: "1.0"
- top-k: "0"
- jinja: ""
- flash-attn: "on"

</details>

## [gpt-oss:20b](https://huggingface.co/ggml-org/gpt-oss-20b-GGUF)
```bash
llamate add gpt-oss:20b
```
<details> <summary>parameters</summary>

- ctx-size: "16384"
- temp: "1.0"
- top-p: "1.0"
- top-k: "0"
- jinja: ""
- flash-attn: "on"

</details>

## [qwen3-coder:30b-a3b](https://huggingface.co/unsloth/Qwen3-Coder-30B-A3B-Instruct-GGUF)
```bash
llamate add qwen3-coder:30b-a3b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.7"
- top-p: "0.8"
- top-k: "20"
- min-p: "0.00"
- jinja: ""
- flash-attn: "on"
- repeat-penalty: "1.05"

</details>

## [qwen3-think:30b-a3b](https://huggingface.co/unsloth/Qwen3-30B-A3B-Thinking-2507-GGUF)
```bash
llamate add qwen3-think:30b-a3b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"
- jinja: ""
- flash-attn: "on"
- presence-penalty: "0.5"

</details>

## [qwen3:30b-a3b](https://huggingface.co/unsloth/Qwen3-30B-A3B-Instruct-2507-GGUF)
```bash
llamate add qwen3:30b-a3b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.7"
- top-p: "0.8"
- top-k: "20"
- min-p: "0.0"
- jinja: ""
- flash-attn: "on"
- presence-penalty: "0.5"

</details>

## [glm-4.1:9b](https://huggingface.co/unsloth/GLM-4.1V-9B-Thinking-GGUF)
```bash
llamate add glm-4.1:9b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [magistral:small](https://huggingface.co/unsloth/Magistral-Small-2507-GGUF)
```bash
llamate add magistral:small
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.7"
- top-p: "0.95"
- jinja: ""
- flash-attn: "on"

</details>

## [openreasoning-nemotron:32b](https://huggingface.co/bartowski/nvidia_OpenReasoning-Nemotron-32B-GGUF)
```bash
llamate add openreasoning-nemotron:32b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [openreasoning-nemotron:14b](https://huggingface.co/bartowski/nvidia_OpenReasoning-Nemotron-14B-GGUF)
```bash
llamate add openreasoning-nemotron:14b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [openreasoning-nemotron:7b](https://huggingface.co/bartowski/nvidia_OpenReasoning-Nemotron-7B-GGUF)
```bash
llamate add openreasoning-nemotron:7b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [openreasoning-nemotron:1.5b](https://huggingface.co/bartowski/nvidia_OpenReasoning-Nemotron-1.5B-GGUF)
```bash
llamate add openreasoning-nemotron:1.5b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [exaone-4:32b](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-32B-GGUF)
```bash
llamate add exaone-4:32b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- top-p: "0.95"
- temp: "0.6"
- jinja: ""
- flash-attn: "on"

</details>

## [hunyuan:a13b](https://huggingface.co/unsloth/Hunyuan-A13B-Instruct-GGUF)
```bash
llamate add hunyuan:a13b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- repeat-penalty: "1.05"
- top-k: "20"
- top-p: "0.8"
- temp: "0.7"
- jinja: ""
- flash-attn: "on"

</details>

## [code-nemotron:32b](https://huggingface.co/mradermacher/OpenCodeReasoning-Nemotron-1.1-32B-GGUF)
```bash
llamate add code-nemotron:32b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- top-p: "0.95"
- temp: "0.6"
- jinja: ""
- flash-attn: "on"

</details>

## [code-nemotron:14b](https://huggingface.co/mradermacher/OpenCodeReasoning-Nemotron-1.1-14B-GGUF)
```bash
llamate add code-nemotron:14b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- top-p: "0.95"
- temp: "0.6"
- jinja: ""
- flash-attn: "on"

</details>

## [code-nemotron:7b](https://huggingface.co/mradermacher/OpenCodeReasoning-Nemotron-1.1-7B-GGUF)
```bash
llamate add code-nemotron:7b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- top-p: "0.95"
- temp: "0.6"
- jinja: ""
- flash-attn: "on"

</details>

## [phi4:reasoning-plus](https://huggingface.co/unsloth/Phi-4-reasoning-plus-GGUF)
```bash
llamate add phi4:reasoning-plus
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- temp: "0.8"
- top-p: "0.95"
- flash-attn: "on"

</details>

## [llama3:8b](https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF)
```bash
llamate add llama3:8b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [llama3_1:8b](https://huggingface.co/unsloth/Llama-3.1-8B-Instruct-GGUF)
```bash
llamate add llama3_1:8b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [llama3_2:1b](https://huggingface.co/unsloth/Llama-3.2-1B-Instruct-GGUF)
```bash
llamate add llama3_2:1b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [llama3_2:3b](https://huggingface.co/unsloth/Llama-3.2-3B-Instruct-GGUF)
```bash
llamate add llama3_2:3b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [llama3_3:70b](https://huggingface.co/unsloth/Llama-3.3-70B-Instruct-GGUF)
```bash
llamate add llama3_3:70b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [llama3_1-nemotron-nano:8b](https://huggingface.co/unsloth/Llama-3.1-Nemotron-Nano-8B-v1-GGUF)
```bash
llamate add llama3_1-nemotron-nano:8b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [acereason-nemotron:14b](https://huggingface.co/unsloth/AceReason-Nemotron-14B-GGUF)
```bash
llamate add acereason-nemotron:14b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- temp: "0.6"
- top-p: "0.95"
- flash-attn: "on"

</details>

## [acereason-nemotron:7b](https://huggingface.co/bartowski/nvidia_AceReason-Nemotron-1.1-7B-GGUF)
```bash
llamate add acereason-nemotron:7b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- temp: "0.6"
- top-p: "0.95"
- flash-attn: "on"

</details>

## [llama3_3-nemotron-super:49b](https://huggingface.co/unsloth/Llama-3_3-Nemotron-Super-49B-v1-GGUF)
```bash
llamate add llama3_3-nemotron-super:49b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [r1-distill:8b](https://huggingface.co/unsloth/DeepSeek-R1-0528-Qwen3-8B-GGUF)
```bash
llamate add r1-distill:8b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [mistral:small-3_1](https://huggingface.co/unsloth/Mistral-Small-3.1-24B-Instruct-2503-GGUF)
```bash
llamate add mistral:small-3_1
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.15"
- jinja: ""
- flash-attn: "on"

</details>

## [mistral:small-3_2](https://huggingface.co/unsloth/Mistral-Small-3.2-24B-Instruct-2506-GGUF)
```bash
llamate add mistral:small-3_2
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.15"
- jinja: ""
- top-p: "1.00"
- flash-attn: "on"

</details>

## [devstral:small](https://huggingface.co/unsloth/Devstral-Small-2507-GGUF)
```bash
llamate add devstral:small
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- temp: "0.15"
- min-p: "0.01"
- top-p: "0.95"
- top-k: "64"
- repeat-penalty: "1.0"
- flash-attn: "on"

</details>

## [qwen3:32b](https://huggingface.co/unsloth/Qwen3-32B-GGUF)
```bash
llamate add qwen3:32b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"
- jinja: ""
- flash-attn: "on"

</details>

## [qwen3:14b](https://huggingface.co/unsloth/Qwen3-14B-GGUF)
```bash
llamate add qwen3:14b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"
- jinja: ""
- flash-attn: "on"

</details>

## [qwen3:8b](https://huggingface.co/unsloth/Qwen3-8B-GGUF)
```bash
llamate add qwen3:8b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"
- jinja: ""
- flash-attn: "on"

</details>

## [qwen3:4b](https://huggingface.co/unsloth/Qwen3-4B-GGUF)
```bash
llamate add qwen3:4b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"
- jinja: ""
- flash-attn: "on"

</details>

## [qwen3:1_7b](https://huggingface.co/unsloth/Qwen3-1.7B-GGUF)
```bash
llamate add qwen3:1_7b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"
- jinja: ""
- flash-attn: "on"

</details>

## [qwen3:0_6b](https://huggingface.co/unsloth/Qwen3-0.6B-GGUF)
```bash
llamate add qwen3:0_6b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- top-k: "20"
- min-p: "0.0"
- jinja: ""
- flash-attn: "on"

</details>

## [r1-distill-qwen:32b](https://huggingface.co/unsloth/DeepSeek-R1-Distill-Qwen-32B-GGUF)
```bash
llamate add r1-distill-qwen:32b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- jinja: ""
- flash-attn: "on"

</details>

## [gemma3:27b](https://huggingface.co/unsloth/gemma-3-27b-it-qat-GGUF)
```bash
llamate add gemma3:27b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [gemma3:12b](https://huggingface.co/unsloth/gemma-3-12b-it-qat-GGUF)
```bash
llamate add gemma3:12b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [gemma3:4b](https://huggingface.co/unsloth/gemma-3-4b-it-qat-GGUF)
```bash
llamate add gemma3:4b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [gemma3:1b](https://huggingface.co/unsloth/gemma-3-1b-it-GGUF)
```bash
llamate add gemma3:1b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [qwq:32b](https://huggingface.co/unsloth/QwQ-32B-GGUF)
```bash
llamate add qwq:32b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- repeat-penalty: "1.1"
- dry-multiplier: "0.5"
- min-p: "0.01"
- top-k: "40"
- top-p: "0.95"
- samplers: "top_k;top_p;min_p;temperature;dry;typ_p;xtc"
- jinja: ""
- flash-attn: "on"

</details>

## [jan-nano](https://huggingface.co/unsloth/Jan-nano-GGUF)
```bash
llamate add jan-nano
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [jan-nano:q8](https://huggingface.co/unsloth/Jan-nano-GGUF)
```bash
llamate add jan-nano:q8
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [seed-coder:8b](https://huggingface.co/unsloth/Seed-Coder-8B-Instruct-GGUF)
```bash
llamate add seed-coder:8b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [seed-coder-reasoning:8b](https://huggingface.co/unsloth/Seed-Coder-8B-Reasoning-GGUF)
```bash
llamate add seed-coder-reasoning:8b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [deepcoder-14b-preview](https://huggingface.co/bartowski/agentica-org_DeepCoder-14B-Preview-GGUF)
```bash
llamate add deepcoder-14b-preview
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- temp: "0.6"
- top-p: "0.95"
- jinja: ""
- flash-attn: "on"

</details>

## [skywork-swe:32b](https://huggingface.co/bartowski/Skywork_Skywork-SWE-32B-GGUF)
```bash
llamate add skywork-swe:32b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [kimi-dev:72b](https://huggingface.co/unsloth/Kimi-Dev-72B-GGUF)
```bash
llamate add kimi-dev:72b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>

## [openbuddy-r1-distill-preview:32b](https://huggingface.co/bartowski/OpenBuddy_OpenBuddy-R1-0528-Distill-Qwen3-32B-Preview0-QAT-GGUF)
```bash
llamate add openbuddy-r1-distill-preview:32b
```
<details> <summary>parameters</summary>

- ctx-size: "8192"
- jinja: ""
- flash-attn: "on"

</details>
