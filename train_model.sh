#!/usr/bin/env bash

echo "Training model"

python3 train_code.py \
    --model_name meta-llama/Llama-2-7b-hf \
    --load_in_4bit \
    --batch_size 2 \
    --gradient_accumulation_steps 2 \
    --num_train_epochs 5 \
    --use_peft \
    --output_dir architecture-model2 \
    --learning_rate 0.0005 \
    --seq_length 1024 \
    --peft_lora_alpha 100 \
    --peft_lora_r 100