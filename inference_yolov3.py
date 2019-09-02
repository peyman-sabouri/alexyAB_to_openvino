from .yolo_utils import ParseYOLOV3Output, IntersectionOverUnion

for frame_results in detections:
    print(frame_results.keys())
    frame_number = frame_results["frame_id"]
    frame_height = frame_results["frame_height"]
    frame_width = frame_results["frame_width"]
    objects = []
    for output in frame_results["detections"].values():
        print ("len _ objects =======", len(objects))
        objects = ParseYOLOV3Output(output,416, 416, frame_height, frame_width, 0.8, objects)
        objlen = len(objects)
        for i in range(objlen):
            print (objects[i].confidence)
            if (objects[i].confidence == 0.2):
                continue
            for j in range(i + 1, objlen):
                if (IntersectionOverUnion(objects[i], objects[j]) >= 0.2):
                    if objects[i].confidence < objects[j].confidence:
                        objects[i], objects[j] = objects[j], objects[i]
                    objects[j].confidence = 0.0
    for obj in objects:
        if obj.confidence < 0.2:
            continue
        label = int(obj.class_id)
        confidence = obj.confidence
           
        if obj.xmin < 0:
            obj.xmin = 0
        if obj.ymin < 0 :
            obj.ymin = 0 

        results.add_box(
            "{:.1f}".format(obj.xmin),
            "{:.1f}".format(obj.ymin),
            "{:.1f}".format(obj.xmax),
            "{:.1f}".format(obj.ymax),
            label,frame_number,)
    
