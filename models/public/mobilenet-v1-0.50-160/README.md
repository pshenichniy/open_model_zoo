# mobilenet-v1-0.50-160

## Use Case and High-Level Description

`mobilenet-v1-0.50-160` is one of MobileNets - small, low-latency, low-power models parameterized to meet the resource constraints of a variety of use cases. They can be built upon for classification, detection, embeddings and segmentation similar to how other popular large scale models are used. For details, see [paper](https://arxiv.org/abs/1704.04861).

## Specification

| Metric                          | Value                                     |
|---------------------------------|-------------------------------------------|
| Type                            | Classification                            |
| GFlops                          | 0.156                                     |
| MParams                         | 1.327                                     |
| Source framework                | TensorFlow\*                              |

## Accuracy

| Metric | Value |
| ------ | ----- |
| Top 1  | 59.86%|
| Top 5  | 82.04%|

## Input

### Original Model

Image, name: `input`, shape: `1, 160, 160, 3`, format: `B, H, W, C`, where:

- `B` - batch size
- `H` - image height
- `W` - image width
- `C` - number of channels

Expected color order: `RGB`.
Mean values: [127.5, 127.5, 127.5], scale factor for each channel: 127.5

### Converted Model

Image, name: `input`, shape: `1, 3, 160, 160`, format: `B, C, H, W`  where:

- `B` - batch size
- `C` - number of channels
- `H` - image height
- `W` - image width

Expected color order: `BGR`.

## Output

### Original Model

Probabilities for all dataset classes in [0, 1] range (0 class is background). Name: `MobilenetV1/Predictions/Reshape_1`.

### Converted Model

Probabilities for all dataset classes in [0, 1] range (0 class is background). Name: `MobilenetV1/Predictions/Softmax`, shape: `1, 1001`, format: `B, C`, where:

- `B` - batch size
- `C` - vector of probabilities.

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
[Apache License, Version 2.0](https://raw.githubusercontent.com/tensorflow/models/master/LICENSE).
A copy of the license is provided in `<omz_dir>/models/public/licenses/APACHE-2.0-TF-Models.txt`.
