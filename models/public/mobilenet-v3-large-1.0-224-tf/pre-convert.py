#!/usr/bin/env python3

# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import tensorflow as tf

from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', type=Path)
    parser.add_argument('output_dir', type=Path)
    args = parser.parse_args()

    tf.keras.backend.set_image_data_format('channels_last')

    model = tf.keras.applications.MobileNetV3Large(
        weights=str(args.input_dir / 'weights_mobilenet_v3_large_224_1.0_float.h5')
    )
    model.save(filepath=args.output_dir/ 'mobilenet_v3_large_224_1.0_float.savedmodel')


if __name__ == '__main__':
    main()
