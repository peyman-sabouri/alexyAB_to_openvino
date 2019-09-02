# Instruction for converting alexy_ab (darknet) to openvino

## 1. Darknet to tensorflow
[darknet to tensorflow](https://github.com/mystic123/tensorflow-yolo-v3.git )
```console
git clone https://github.com/mystic123/tensorflow-yolo-v3.git
```
### Convert yolo_tiny_v3 to tensorflow
```console
$ python3 convert_weights_pb.py     --weights_file ../alexyAB_weights/yolov3-tiny_5000.weights  --class_names ../alexyAB_weights/voc.names         --data_format NHWC   --tiny   --output_graph custom_tiny_yolov3.pb --size 416
```

```console
 python3 ./demo.py --input_img python3 ./demo.py --input_img  test.jpg  --output_img ./yoloOutput.jpg --frozen_model custom_tiny_yolov3.pb   --class_names ../alexyAB_weights/voc.names 
```
### Test:
```console
$ python3 ./demo.py --input_img python3 ./demo.py --input_img  test.jpg \ --output_img ./yoloOutput.jpg --frozen_model custom_tiny_yolov3.pb \  --class_names ../alexyAB_weights/voc.names 
```
## 2. Tensorflow to openvino 

```console
$ python3 /opt/intel/computer_vision_sdk/deployment_tools/model_optimizer/mo_tf.py  --input_model  /home/peyman/mnt/data/DATA/Deep_learning/openvino_stuff/tensorflow-yolo-v3/custom_tiny_yolov3.pb --tensorflow_use_custom_operations_config extensions/front/tf/yolo_v3_tiny.json  --batch 1 --output_dr ../../../Deep_learning/openvino_stuff/new_model/  --data_type FP32 --reverse_input_channels
```


### Test openino in CVAT:

```console
docker exec -it cvat  bash -ic 'python3 ~/cvat/apps/auto_annotation/run_model.py --py ~/cvat/apps/auto_annotation/custom_yolo/new_test_vino/inference_yolov3.py  --xml ~/cvat/apps/auto_annotation/custom_yolo/new_test_vino/custom_tiny_yolov3.xml --bin ~/cvat/apps/auto_annotation/custom_yolo/new_test_vino/custom_tiny_yolov3.bin --json ~/cvat/apps/auto_annotation/custom_yolo/new_test_vino/map.json  --unrestricted --show-images --image-files ~/cvat/apps/auto_annotation/test.jpg' 
```
