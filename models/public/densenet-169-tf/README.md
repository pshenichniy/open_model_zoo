# densenet-169-tf

## Use Case and High-Level Description

This is a TensorFlow\* version of `densenet-169` model, one of the DenseNet group of models designed to perform image classification.
For details, see [TensorFlow\* API docs](https://www.tensorflow.org/api_docs/python/tf/keras/applications/DenseNet169), [repository](https://github.com/tensorflow/tensorflow) and [paper](https://arxiv.org/abs/1608.06993).

## Specification

| Metric                          | Value           |
|---------------------------------|-----------------|
| Type                            | Classification  |
| GFlops                          | 6.7932          |
| MParams                         | 14.1389         |
| Source framework                | TensorFlow\*    |

## Accuracy

| Metric | Value |
| ------ | ----- |
| Top 1  | 76.14%|
| Top 5  | 93.12%|

## Input

### Original Model

Image, name: `input_1`, shape: `1, 224, 224, 3`, format: `B, H, W, C`, where:

- `B` - batch size
- `H` - image height
- `W` - image width
- `C` - number of channels

Expected color order: `RGB`.
Mean values - [123.68, 116.78, 103.94], scale values - [58.395,57.12,57.375].

### Converted Model

Image, name: `input_1`, shape: `1, 3, 224, 224`, format: `B, C, H, W`, where:

- `B` - batch size
- `C` - number of channels
- `H` - image height
- `W` - image width

Expected color order: `BGR`.

## Output

### Original Model

Object classifier according to ImageNet classes, name: `StatefulPartitionedCall/densenet169/predictions/Softmax`,  shape: `1, 1000`, output data format is `B, C`, where:

- `B` - batch size
- `C` - predicted probabilities for each class in  [0, 1] range

### Converted Model

The converted model has the same parameters as the original model.

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
[Apache License, Version 2.0](https://raw.githubusercontent.com/tensorflow/tensorflow/master/LICENSE).
A copy of the license is provided in `<omz_dir>/models/public/licenses/APACHE-2.0-TensorFlow.txt`.
