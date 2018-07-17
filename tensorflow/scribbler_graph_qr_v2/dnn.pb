node {
  name: "image_tensor"
  op: "Placeholder"
  attr {
    key: "dtype"
    value {
      type: DT_UINT8
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_0/Conv2D"
  op: "Conv2D"
  input: "image_tensor"
  input: "FeatureExtractor/MobilenetV1/Conv2d_0/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_0/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_0/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_0/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_0/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_0/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_0/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_1_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_1_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_1_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_1_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_1_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_1_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_1_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_2_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_2_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_2_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_2_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_2_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_2_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_2_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_3_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_3_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_3_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_3_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_3_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_3_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_3_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_4_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_4_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_4_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_4_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_4_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_4_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_4_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_5_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_5_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_5_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_5_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_5_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_5_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_5_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_6_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_6_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_6_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_6_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_6_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_6_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_6_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_7_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_7_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_7_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_7_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_7_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_7_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_7_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_8_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_8_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_8_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_8_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_8_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_8_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_8_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_9_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_9_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_9_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_9_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_9_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_9_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_9_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_10_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_10_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_10_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_10_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_10_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_10_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_10_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_11_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_11_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_11_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_11_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_11_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_11_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "BoxPredictor_0/ClassPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/Relu6"
  input: "BoxPredictor_0/ClassPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_0/ClassPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_0/ClassPredictor/Conv2D"
  input: "BoxPredictor_0/ClassPredictor/biases"
}
node {
  name: "BoxPredictor_0/BoxEncodingPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/Relu6"
  input: "BoxPredictor_0/BoxEncodingPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_0/BoxEncodingPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_0/BoxEncodingPredictor/Conv2D"
  input: "BoxPredictor_0/BoxEncodingPredictor/biases"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_11_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_12_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_12_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_12_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_12_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_12_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_12_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_depthwise/depthwise"
  op: "DepthwiseConv2dNative"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_12_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_depthwise/depthwise_weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_depthwise/BatchNorm/FusedBatchNorm"
  op: "FusedBatchNorm"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_depthwise/depthwise"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_depthwise/BatchNorm/gamma"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_depthwise/BatchNorm/beta"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_depthwise/BatchNorm/moving_mean"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_depthwise/BatchNorm/moving_variance"
  attr {
    key: "epsilon"
    value {
      f: 0.0010000000475
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_depthwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_depthwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_depthwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_2_1x1_256/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_2_1x1_256/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_2_1x1_256/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_2_1x1_256/Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_2_1x1_256/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_2_1x1_256/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_2_1x1_256/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_2_1x1_256/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_3_1x1_128/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_3_1x1_128/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_3_1x1_128/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_3_1x1_128/Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_3_1x1_128/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_3_1x1_128/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_3_1x1_128/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_3_1x1_128/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_4_1x1_128/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_4_1x1_128/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_4_1x1_128/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_4_1x1_128/Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_4_1x1_128/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_4_1x1_128/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_4_1x1_128/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_4_1x1_128/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_5_1x1_64/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_5_1x1_64/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_5_1x1_64/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_5_1x1_64/Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_5_1x1_64/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_5_1x1_64/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_5_1x1_64/BatchNorm/FusedBatchNorm"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_1_Conv2d_5_1x1_64/Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 2
        i: 2
        i: 1
      }
    }
  }
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/BatchNorm/FusedBatchNorm"
  op: "BiasAdd"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/Conv2D_bn_offset"
}
node {
  name: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/Relu6"
  op: "Relu6"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/BatchNorm/FusedBatchNorm"
}
node {
  name: "BoxPredictor_5/ClassPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/Relu6"
  input: "BoxPredictor_5/ClassPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_5/ClassPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_5/ClassPredictor/Conv2D"
  input: "BoxPredictor_5/ClassPredictor/biases"
}
node {
  name: "BoxPredictor_5/BoxEncodingPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_5_3x3_s2_128/Relu6"
  input: "BoxPredictor_5/BoxEncodingPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_5/BoxEncodingPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_5/BoxEncodingPredictor/Conv2D"
  input: "BoxPredictor_5/BoxEncodingPredictor/biases"
}
node {
  name: "BoxPredictor_4/ClassPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/Relu6"
  input: "BoxPredictor_4/ClassPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_4/ClassPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_4/ClassPredictor/Conv2D"
  input: "BoxPredictor_4/ClassPredictor/biases"
}
node {
  name: "BoxPredictor_4/BoxEncodingPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_4_3x3_s2_256/Relu6"
  input: "BoxPredictor_4/BoxEncodingPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_4/BoxEncodingPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_4/BoxEncodingPredictor/Conv2D"
  input: "BoxPredictor_4/BoxEncodingPredictor/biases"
}
node {
  name: "BoxPredictor_3/ClassPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/Relu6"
  input: "BoxPredictor_3/ClassPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_3/ClassPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_3/ClassPredictor/Conv2D"
  input: "BoxPredictor_3/ClassPredictor/biases"
}
node {
  name: "BoxPredictor_3/BoxEncodingPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_3_3x3_s2_256/Relu6"
  input: "BoxPredictor_3/BoxEncodingPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_3/BoxEncodingPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_3/BoxEncodingPredictor/Conv2D"
  input: "BoxPredictor_3/BoxEncodingPredictor/biases"
}
node {
  name: "BoxPredictor_2/ClassPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/Relu6"
  input: "BoxPredictor_2/ClassPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_2/ClassPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_2/ClassPredictor/Conv2D"
  input: "BoxPredictor_2/ClassPredictor/biases"
}
node {
  name: "BoxPredictor_2/BoxEncodingPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/Conv2d_13_pointwise_2_Conv2d_2_3x3_s2_512/Relu6"
  input: "BoxPredictor_2/BoxEncodingPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_2/BoxEncodingPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_2/BoxEncodingPredictor/Conv2D"
  input: "BoxPredictor_2/BoxEncodingPredictor/biases"
}
node {
  name: "BoxPredictor_1/ClassPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/Relu6"
  input: "BoxPredictor_1/ClassPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_1/ClassPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_1/ClassPredictor/Conv2D"
  input: "BoxPredictor_1/ClassPredictor/biases"
}
node {
  name: "BoxPredictor_1/BoxEncodingPredictor/Conv2D"
  op: "Conv2D"
  input: "FeatureExtractor/MobilenetV1/MobilenetV1/Conv2d_13_pointwise/Relu6"
  input: "BoxPredictor_1/BoxEncodingPredictor/weights"
  attr {
    key: "dilations"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
  attr {
    key: "padding"
    value {
      s: "SAME"
    }
  }
  attr {
    key: "strides"
    value {
      list {
        i: 1
        i: 1
        i: 1
        i: 1
      }
    }
  }
}
node {
  name: "BoxPredictor_1/BoxEncodingPredictor/BiasAdd"
  op: "BiasAdd"
  input: "BoxPredictor_1/BoxEncodingPredictor/Conv2D"
  input: "BoxPredictor_1/BoxEncodingPredictor/biases"
}
node {
  name: "concat/axis_flatten"
  op: "Const"
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: -1
      }
    }
  }
}
node {
  name: "PriorBox/concat/axis"
  op: "Const"
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 1
          }
        }
        int_val: -2
      }
    }
  }
}
node {
  name: "BoxPredictor_0/ClassPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_0/ClassPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_1/ClassPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_1/ClassPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_2/ClassPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_2/ClassPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_3/ClassPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_3/ClassPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_4/ClassPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_4/ClassPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_5/ClassPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_5/ClassPredictor/BiasAdd"
}
node {
  name: "ClassPredictor/concat"
  op: "ConcatV2"
  input: "BoxPredictor_0/ClassPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_1/ClassPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_2/ClassPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_3/ClassPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_4/ClassPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_5/ClassPredictor/BiasAdd/Flatten"
  input: "concat/axis_flatten"
}
node {
  name: "BoxPredictor_0/BoxEncodingPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_0/BoxEncodingPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_1/BoxEncodingPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_1/BoxEncodingPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_2/BoxEncodingPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_2/BoxEncodingPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_3/BoxEncodingPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_3/BoxEncodingPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_4/BoxEncodingPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_4/BoxEncodingPredictor/BiasAdd"
}
node {
  name: "BoxPredictor_5/BoxEncodingPredictor/BiasAdd/Flatten"
  op: "Flatten"
  input: "BoxPredictor_5/BoxEncodingPredictor/BiasAdd"
}
node {
  name: "BoxEncodingPredictor/concat"
  op: "ConcatV2"
  input: "BoxPredictor_0/BoxEncodingPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_1/BoxEncodingPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_2/BoxEncodingPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_3/BoxEncodingPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_4/BoxEncodingPredictor/BiasAdd/Flatten"
  input: "BoxPredictor_5/BoxEncodingPredictor/BiasAdd/Flatten"
  input: "concat/axis_flatten"
}
node {
  name: "reshape_prior_boxes_to_4d"
  op: "Const"
  attr {
    key: "value"
    value {
      tensor {
        dtype: DT_INT32
        tensor_shape {
          dim {
            size: 4
          }
        }
        int_val: 1
        int_val: 2
        int_val: -1
        int_val: 1
      }
    }
  }
}
node {
  name: "PriorBox_0"
  op: "PriorBox"
  input: "BoxPredictor_0/BoxEncodingPredictor/BiasAdd"
  input: "image_tensor"
  attr {
    key: "clip"
    value {
      b: false
    }
  }
  attr {
    key: "flip"
    value {
      b: false
    }
  }
  attr {
    key: "height"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 3
          }
        }
        float_val: 30.0
        float_val: 42.4264068604
        float_val: 84.8528137207
      }
    }
  }
  attr {
    key: "variance"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 4
          }
        }
        float_val: 0.10000000149
        float_val: 0.10000000149
        float_val: 0.20000000298
        float_val: 0.20000000298
      }
    }
  }
  attr {
    key: "width"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 3
          }
        }
        float_val: 30.0
        float_val: 84.8528137207
        float_val: 42.4264068604
      }
    }
  }
}
node {
  name: "PriorBox_0/4d"
  op: "Reshape"
  input: "PriorBox_0"
  input: "reshape_prior_boxes_to_4d"
}
node {
  name: "PriorBox_1"
  op: "PriorBox"
  input: "BoxPredictor_1/BoxEncodingPredictor/BiasAdd"
  input: "image_tensor"
  attr {
    key: "clip"
    value {
      b: false
    }
  }
  attr {
    key: "flip"
    value {
      b: false
    }
  }
  attr {
    key: "height"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 105.0
        float_val: 74.2462158203
        float_val: 148.492431641
        float_val: 60.6217765808
        float_val: 181.956329346
        float_val: 125.499000549
      }
    }
  }
  attr {
    key: "variance"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 4
          }
        }
        float_val: 0.10000000149
        float_val: 0.10000000149
        float_val: 0.20000000298
        float_val: 0.20000000298
      }
    }
  }
  attr {
    key: "width"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 105.0
        float_val: 148.492431641
        float_val: 74.2462158203
        float_val: 181.865341187
        float_val: 60.5914611816
        float_val: 125.499000549
      }
    }
  }
}
node {
  name: "PriorBox_1/4d"
  op: "Reshape"
  input: "PriorBox_1"
  input: "reshape_prior_boxes_to_4d"
}
node {
  name: "PriorBox_2"
  op: "PriorBox"
  input: "BoxPredictor_2/BoxEncodingPredictor/BiasAdd"
  input: "image_tensor"
  attr {
    key: "clip"
    value {
      b: false
    }
  }
  attr {
    key: "flip"
    value {
      b: false
    }
  }
  attr {
    key: "height"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 150.0
        float_val: 106.066017151
        float_val: 212.132034302
        float_val: 86.6025390625
        float_val: 259.93762207
        float_val: 171.026306152
      }
    }
  }
  attr {
    key: "variance"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 4
          }
        }
        float_val: 0.10000000149
        float_val: 0.10000000149
        float_val: 0.20000000298
        float_val: 0.20000000298
      }
    }
  }
  attr {
    key: "width"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 150.0
        float_val: 212.132034302
        float_val: 106.066017151
        float_val: 259.807617188
        float_val: 86.5592269897
        float_val: 171.026306152
      }
    }
  }
}
node {
  name: "PriorBox_2/4d"
  op: "Reshape"
  input: "PriorBox_2"
  input: "reshape_prior_boxes_to_4d"
}
node {
  name: "PriorBox_3"
  op: "PriorBox"
  input: "BoxPredictor_3/BoxEncodingPredictor/BiasAdd"
  input: "image_tensor"
  attr {
    key: "clip"
    value {
      b: false
    }
  }
  attr {
    key: "flip"
    value {
      b: false
    }
  }
  attr {
    key: "height"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 195.0
        float_val: 137.885818481
        float_val: 275.771636963
        float_val: 112.583305359
        float_val: 337.918914795
        float_val: 216.333084106
      }
    }
  }
  attr {
    key: "variance"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 4
          }
        }
        float_val: 0.10000000149
        float_val: 0.10000000149
        float_val: 0.20000000298
        float_val: 0.20000000298
      }
    }
  }
  attr {
    key: "width"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 195.0
        float_val: 275.771636963
        float_val: 137.885818481
        float_val: 337.749908447
        float_val: 112.527000427
        float_val: 216.333084106
      }
    }
  }
}
node {
  name: "PriorBox_3/4d"
  op: "Reshape"
  input: "PriorBox_3"
  input: "reshape_prior_boxes_to_4d"
}
node {
  name: "PriorBox_4"
  op: "PriorBox"
  input: "BoxPredictor_4/BoxEncodingPredictor/BiasAdd"
  input: "image_tensor"
  attr {
    key: "clip"
    value {
      b: false
    }
  }
  attr {
    key: "flip"
    value {
      b: false
    }
  }
  attr {
    key: "height"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 240.0
        float_val: 169.705627441
        float_val: 339.411254883
        float_val: 138.564071655
        float_val: 415.90020752
        float_val: 261.533935547
      }
    }
  }
  attr {
    key: "variance"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 4
          }
        }
        float_val: 0.10000000149
        float_val: 0.10000000149
        float_val: 0.20000000298
        float_val: 0.20000000298
      }
    }
  }
  attr {
    key: "width"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 240.0
        float_val: 339.411254883
        float_val: 169.705627441
        float_val: 415.692199707
        float_val: 138.494766235
        float_val: 261.533935547
      }
    }
  }
}
node {
  name: "PriorBox_4/4d"
  op: "Reshape"
  input: "PriorBox_4"
  input: "reshape_prior_boxes_to_4d"
}
node {
  name: "PriorBox_5"
  op: "PriorBox"
  input: "BoxPredictor_5/BoxEncodingPredictor/BiasAdd"
  input: "image_tensor"
  attr {
    key: "clip"
    value {
      b: false
    }
  }
  attr {
    key: "flip"
    value {
      b: false
    }
  }
  attr {
    key: "height"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 285.0
        float_val: 201.525436401
        float_val: 403.050872803
        float_val: 164.544830322
        float_val: 493.881469727
        float_val: 292.403839111
      }
    }
  }
  attr {
    key: "variance"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 4
          }
        }
        float_val: 0.10000000149
        float_val: 0.10000000149
        float_val: 0.20000000298
        float_val: 0.20000000298
      }
    }
  }
  attr {
    key: "width"
    value {
      tensor {
        dtype: DT_FLOAT
        tensor_shape {
          dim {
            size: 6
          }
        }
        float_val: 285.0
        float_val: 403.050872803
        float_val: 201.525436401
        float_val: 493.634490967
        float_val: 164.462539673
        float_val: 292.403839111
      }
    }
  }
}
node {
  name: "PriorBox_5/4d"
  op: "Reshape"
  input: "PriorBox_5"
  input: "reshape_prior_boxes_to_4d"
}
node {
  name: "PriorBox/concat"
  op: "ConcatV2"
  input: "PriorBox_0/4d"
  input: "PriorBox_1/4d"
  input: "PriorBox_2/4d"
  input: "PriorBox_3/4d"
  input: "PriorBox_4/4d"
  input: "PriorBox_5/4d"
  input: "PriorBox/concat/axis"
}
node {
  name: "ClassPredictor/concat/sigmoid"
  op: "Sigmoid"
  input: "ClassPredictor/concat"
}
node {
  name: "detection_out"
  op: "DetectionOutput"
  input: "BoxEncodingPredictor/concat"
  input: "ClassPredictor/concat/sigmoid"
  input: "PriorBox/concat"
  attr {
    key: "background_label_id"
    value {
      i: 0
    }
  }
  attr {
    key: "code_type"
    value {
      s: "CENTER_SIZE"
    }
  }
  attr {
    key: "confidence_threshold"
    value {
      f: 0.00999999977648
    }
  }
  attr {
    key: "keep_top_k"
    value {
      i: 100
    }
  }
  attr {
    key: "loc_pred_transposed"
    value {
      b: true
    }
  }
  attr {
    key: "nms_threshold"
    value {
      f: 0.600000023842
    }
  }
  attr {
    key: "num_classes"
    value {
      i: 91
    }
  }
  attr {
    key: "share_location"
    value {
      b: true
    }
  }
  attr {
    key: "top_k"
    value {
      i: 100
    }
  }
}
library {
}
