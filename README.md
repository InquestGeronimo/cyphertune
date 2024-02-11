<div align="center">
    <img width="400" height="350" src="/img/cyphertune-logo.webp">
</div>
<br>

CypherTune is a library for fine-tuning large language models (LLMs) on text-to-Cypher datasets. [Cypher](https://neo4j.com/developer/cypher/) is Neo4j’s graph query language that lets you retrieve data from a knowledge graph. It was inspired by SQL and is the easiest graph language to learn by far because of its similarity to other languages and intuitiveness.

Inspired by Neo4j's recent initiative to crowdsource the first open sourced text-to-Cypher dataset, this repository offers users a simplified and seamless environment for fine-tuning LLMs with a minimal background in AI to get started.

# Features

- **Model Fine-Tuning**: Fine-tune LLMs with custom text-to-cypher datasets from 🤗.
- **Bits and Bytes**: Optimizes model performance with 4-bit quantization.
- **QLoRA**: Fine-tuning using LoRA, a popular and lightweight training technique that significantly reduces the number of trainable parameters
- **Promp Template**: Doc conversion into a prompt template for fine-tuning.
- **Weights & Biases Integration**: Track and log your experiments using wandb. (optional)

Under Development

> - YAML file library storing hyperparameter configurations for select training job environments (i.e. depending on dataset, model type/size and amount of compute).
> - Fully Sharded Data Parallel (FSDP)**: Utilizes FSDP for efficient training across distributed systems.

# Install <img align="center" width="30" height="29" src="https://media.giphy.com/media/sULKEgDMX8LcI/giphy.gif">
<br>

```
pip install cyphertune
```

# Launch CypherTuner <img align="center" width="30" height="29" src="https://media.giphy.com/media/QLcCBdBemDIqpbK6jA/giphy.gif">

To start training, initialize the `CypherTuner` class from the script. Pass along your project name, Hugging Face model stub dataset stubs:

```py
from cyphertune import CypherTuner

trainer = CypherTuner(
    project_name="YourProjectName",
    model_id="ModelIdentifier",
    dataset_id="DatasetIdentifier"
)
```



```
train_data, eval_data = trainer.load_datasets()
model, tokenizer = trainer.load_model_and_tokenizer()
train_data, eval_data = trainer.create_prompts_from_datasets(tokenizer, train_data, eval_data)
model = trainer.configure_lora(model)
trainer = trainer.configure_training(model, tokenizer, train_data, eval_data)
trainer.train_model(trainer)
```

