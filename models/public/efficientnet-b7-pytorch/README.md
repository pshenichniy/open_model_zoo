# efficientnet-b7-pytorch

## Use Case and High-Level Description

The `efficientnet-b7-pytorch` model is one of the [EfficientNet](https://arxiv.org/abs/1905.11946)
models designed to perform image classification. This model was pre-trained in TensorFlow\*, then weights were converted to PyTorch\*. All the EfficientNet models have been pre-trained on the ImageNet image database. For details about this family of models, check out the [EfficientNets for PyTorch repository](https://github.com/rwightman/gen-efficientnet-pytorch).

The model input is a blob that consists of a single image with the `3, 600, 600` shape in the `RGB`
order. Before passing the image blob to the network, do the following:
1. Subtract the RGB mean values as follows: [123.675, 116.28, 103.53]
2. Divide the RGB mean values by  [58.395, 57.12, 57.375]

The model output for `efficientnet-b7-pytorch` is the typical object classifier output for
the 1000 different classifications matching those in the ImageNet database.

## Specification

| Metric            | Value         |
|-------------------|---------------|
| Type              | Classification|
| GFLOPs            | 77.618        |
| MParams           | 66.193        |
| Source framework  | PyTorch\*     |

## Accuracy

| Metric | Original model | Converted model |
| ------ | -------------- | --------------- |
| Top 1  | 84.42%         | 84.42%          |
| Top 5  | 96.91%         | 96.91%          |

## Input

### Original Model

Image, name - `data`,  shape - `1, 3, 600, 600`, format is `B, C, H, W`, where:

- `B` - batch size
- `C` - channel
- `H` - height
- `W` - width

Channel order is `RGB`.
Mean values - [123.675, 116.28, 103.53],  scale values - [58.395, 57.12, 57.375].

### Converted Model

Image, name - `data`,  shape - `1, 3, 600, 600`, format is `B, C, H, W`, where:

- `B` - batch size
- `C` - channel
- `H` - height
- `W` - width

Channel order is `BGR`.

## Output

### Original Model

Object classifier according to ImageNet classes, name - `prob`,  shape - `1, 1000`, output data format is `B, C`, where:

- `B` - batch size
- `C` - predicted probabilities for each class in the logits format

### Converted Model

Object classifier according to ImageNet classes, name - `prob`,  shape - `1, 1000`, output data format is `B, C`, where:

- `B` - batch size
- `C` - predicted probabilities for each class in the logits format

## Download a Model and Convert it into Inference Engine Format

You can download models and if necessary convert them into Inference Engine format using the [Model Downloader and other automation tools](../../../tools/model_tools/README.md) as shown in the examples below.

An example of using the Model Downloader:
```
omz_downloader --name <model_name>
```

An example of using the Model Converter:
```
omz_converter --name <model_name>
```

## Legal Information

The original model is distributed under the
[Apache License, Version 2.0](https://raw.githubusercontent.com/rwightman/gen-efficientnet-pytorch/5e91628ed98250989a7ddd20abfe27385e0493c1/LICENSE).
A copy of the license is provided in `<omz_dir>/models/public/licenses/APACHE-2.0-PyTorch-EfficientNet.txt`.
