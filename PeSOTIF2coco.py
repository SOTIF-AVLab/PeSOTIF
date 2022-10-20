import os
import cv2
import json


def PeSOTIF2coco():
    root_path = './images'
    print("Loading images from ", root_path)
    assert os.path.exists(root_path)
    label_root = './labels'
    folder = './test'
    if not os.path.exists(folder):
        os.makedirs(folder)
    anno_path = './annotations'
    json_name = os.path.join(anno_path, 'PeSOTIF_test.json')

    # preprocess
    test_dataset = {'categories': [], 'annotations': [], 'images': []}
    with open('classes.txt') as f:
        classes = f.read().strip().split()
    for i, cls in enumerate(classes, 0):
        test_dataset['categories'].append({'id': i, 'name': cls, 'supercategory': 'none'})
    img_count = 0
    ann_count = 0
    cer_count = 0
    unc_count = 0

    # data in the Environment set
    set = 'Environment'
    setpath = os.path.join(root_path, set)
    subsets = os.listdir(setpath)
    for subset in subsets:
        for detail in ['Handcraft', 'Natural']:
            imgpaths = os.path.join(os.path.join(setpath, subset), detail)
            indexes = os.listdir(imgpaths)
            prefix = set[: 3] + '_' + subset[: 3] + '_' + detail[: 3] + '_'
            for index in indexes:
                img_count += 1
                img = cv2.imread(os.path.join(imgpaths, index))
                txtFile = index.replace('images', 'txt').replace('.jpg', '.txt').replace('.png', '.txt')
                img_path = os.path.join(folder, prefix + index)
                img_name = prefix + index
                if index.split('.')[1] == 'jpg':
                    cv2.imwrite(img_path, img, [cv2.IMWRITE_JPEG_QUALITY, 100])
                elif index.split('.')[1] == 'png':
                    cv2.imwrite(img_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
                else:
                    cv2.imwrite(img_path, img)
                height, width, _ = img.shape
                test_dataset['images'].append({'file_name': img_name,
                                          'id': img_count,
                                          'width': width,
                                          'height': height})
                label_path = os.path.join(os.path.join(os.path.join(os.path.join(label_root, set), subset), detail), txtFile)
                if not os.path.exists(label_path):
                    # 如没标签，跳过，只保留图片信息。
                    continue
                with open(label_path, 'r') as fr:
                    labelList = fr.readlines()
                    for label in labelList:
                        ann_count += 1
                        label = label.strip().split()
                        x = float(label[1])
                        y = float(label[2])
                        w = float(label[3])
                        h = float(label[4])
                        # convert x,y,w,h to x1,y1,x2,y2
                        H, W, _ = img.shape
                        x1 = (x - w / 2) * W
                        y1 = (y - h / 2) * H
                        x2 = (x + w / 2) * W
                        y2 = (y + h / 2) * H
                        # 标签序号从0开始计算, coco2017数据集标号混乱，不管它了。
                        cls_id = int(label[0])
                        width = max(0, x2 - x1)
                        height = max(0, y2 - y1)
                        difficulty = int(label[5])
                        if difficulty == 0:
                            cer_count += 1
                        elif difficulty == 1:
                            unc_count += 1
                        test_dataset['annotations'].append({
                            'area': width * height,
                            'bbox': [x1, y1, width, height],
                            'category_id': cls_id,
                            'id': ann_count,
                            'image_id': img_count,
                            'iscrowd': 0,
                            # mask, 矩形是从左上角点按顺时针的四个顶点
                            'segmentation': [[x1, y1, x2, y1, x2, y2, x1, y2]],
                        })

    # data in the Object set
    set = 'Object'
    setpath = os.path.join(root_path, set)
    subsets = ['Common/Appearance', 'Common/Posture', 'Uncommon']
    for subset in subsets:
        imgpaths = os.path.join(setpath, subset)
        indexes = os.listdir(imgpaths)
        prefix = set[: 3] + '_'
        pres = subset.split('/')
        for pre in pres:
            prefix = prefix + pre[: 3] + '_'
        for index in indexes:
            img_count += 1
            img = cv2.imread(os.path.join(imgpaths, index))
            txtFile = index.replace('images', 'txt').replace('.jpg', '.txt').replace('.png', '.txt')
            img_path = os.path.join(folder, prefix + index)
            img_name = prefix + index
            if index.split('.')[1] == 'jpg':
                cv2.imwrite(img_path, img, [cv2.IMWRITE_JPEG_QUALITY, 100])
            elif index.split('.')[1] == 'png':
                cv2.imwrite(img_path, img, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            else:
                cv2.imwrite(img_path, img)
            height, width, _ = img.shape
            test_dataset['images'].append({'file_name': img_name,
                                      'id': img_count,
                                      'width': width,
                                      'height': height})
            label_path = os.path.join(os.path.join(os.path.join(label_root, set), subset), txtFile)
            if not os.path.exists(label_path):
                # 如没标签，跳过，只保留图片信息。
                continue
            with open(label_path, 'r') as fr:
                labelList = fr.readlines()
                for label in labelList:
                    ann_count += 1
                    label = label.strip().split()
                    x = float(label[1])
                    y = float(label[2])
                    w = float(label[3])
                    h = float(label[4])
                    # convert x,y,w,h to x1,y1,x2,y2
                    H, W, _ = img.shape
                    x1 = (x - w / 2) * W
                    y1 = (y - h / 2) * H
                    x2 = (x + w / 2) * W
                    y2 = (y + h / 2) * H
                    # 标签序号从0开始计算, coco2017数据集标号混乱，不管它了。
                    cls_id = int(label[0])
                    width = max(0, x2 - x1)
                    height = max(0, y2 - y1)
                    difficulty = int(label[5])
                    if difficulty == 0:
                        cer_count += 1
                    elif difficulty == 1:
                        unc_count += 1
                    test_dataset['annotations'].append({
                        'area': width * height,
                        'bbox': [x1, y1, width, height],
                        'category_id': cls_id,
                        'id': ann_count,
                        'image_id': img_count,
                        'iscrowd': 0,
                        # mask, 矩形是从左上角点按顺时针的四个顶点
                        'segmentation': [[x1, y1, x2, y1, x2, y2, x1, y2]],
                    })
    print('Image counts: ' + str(img_count))
    print('Annotation counts: ' + str(ann_count))
    print('easy objects: ' + str(cer_count))
    print('hard objects: ' + str(unc_count))

    # save
    with open(json_name, 'w') as f:
        json.dump(test_dataset, f)
        print('Save annotation to {}'.format(json_name))


if __name__ == "__main__":
    PeSOTIF2coco()