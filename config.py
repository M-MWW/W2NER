import json
# json是个包，主要用于下面的        with open(args.config, "r", encoding="utf-8") as f:
#             config = json.load(f)
# 剩下的是配置参数类，例：有个config文件，Config(config），先把config文件转换为python对象，
# 剩下的相当于 config.dataset = config["dataset"]，提取配置文件config里的文件

class Config:
    def __init__(self, args):
        with open(args.config, "r", encoding="utf-8") as f:
            config = json.load(f)

        self.dataset = config["dataset"]
        self.save_path = config["save_path"]
        self.predict_path = config["predict_path"]

        self.dist_emb_size = config["dist_emb_size"]
        self.type_emb_size = config["type_emb_size"]
        self.lstm_hid_size = config["lstm_hid_size"]
        self.conv_hid_size = config["conv_hid_size"]
        self.bert_hid_size = config["bert_hid_size"]
        self.biaffine_size = config["biaffine_size"]
        self.ffnn_hid_size = config["ffnn_hid_size"]

        self.dilation = config["dilation"]

        self.emb_dropout = config["emb_dropout"]
        self.conv_dropout = config["conv_dropout"]
        self.out_dropout = config["out_dropout"]

        self.epochs = config["epochs"]
        self.batch_size = config["batch_size"]

        self.learning_rate = config["learning_rate"]
        self.weight_decay = config["weight_decay"]
        self.clip_grad_norm = config["clip_grad_norm"]
        self.bert_name = config["bert_name"]
        self.bert_learning_rate = config["bert_learning_rate"]
        self.warm_factor = config["warm_factor"]

        self.use_bert_last_4_layers = config["use_bert_last_4_layers"]

        self.seed = config["seed"]

        for k, v in args.__dict__.items():
            if v is not None:
                self.__dict__[k] = v

    def __repr__(self):
        return "{}".format(self.__dict__.items())
    # 可以让我快速查看配置对象的所有设置：
