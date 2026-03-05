from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML
model = YOLO("C:\lvdousha\school\graduate_design/bolt_detach\projects\code\yolo11n.pt")  # load a pretrained model (recommended for training)
#model = YOLO("yolo11n.yaml").load("yolo11n.pt")  # build from YAML and transfer weights

if __name__ == '__main__':
# Use the model
    model.train(data="C:\lvdousha\school\graduate_design/bolt_detach\projects\code/train_real\data.yaml", epochs=300, imgsz=640, device='0')  # train the model
    path = model.export(format="onnx")  # export the model to ONNX format
