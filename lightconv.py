import torch

# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'lightconv.glu.wmt17.zh-en', ... ]

# Load a transformer trained on WMT'16 En-De
zh2en = torch.hub.load('pytorch/fairseq', 'lightconv.glu.wmt17.zh-en', tokenizer='moses', bpe='subword_nmt')

# The underlying model is available under the *models* attribute
assert isinstance(zh2en.models[0], fairseq.models.lightconv.LightConvModel)

# Translate a sentence
zh2en.translate('你好 世界')
# 'Hello World'