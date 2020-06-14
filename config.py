class Config:
    visible_gpus = "0,1,2,3"
    idx_text = 1
    idx_label = 6
    vocab_file="./dict/words.txt"
    embedding_size = 64
    epoches = 3
    dropout = 0
    hidden_units = [1024, 512,128, 64]
    train_batch_size = 128
    regularizer_scale = 0.01
    learning_rate = 0.01
    data_dir = "./tfrecords"
    input_files = "part-*[1-9].tfrecord"
    eval_files = "part-*0.tfrecord"
    model_path = "models/dnn"
    label_thres = 0.5
