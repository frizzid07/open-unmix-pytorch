import utils
import torch.hub


# Optional list of dependencies required by the package
dependencies = ['torch', 'numpy']


def umxse(target='speech', device='cpu', pretrained=True, *args, **kwargs):
    """
    Open Unmix Speech Enhancemennt 1-channel BiLSTM Model
    trained on the 28-speaker version of Voicebank+Demand
    (Sampling rate: 16kHz)

    Reference:
        Uhlich, Stefan, & Mitsufuji, Yuki. (2020).
        Open-Unmix for Speech Enhancement (UMX SE).
        Zenodo. http://doi.org/10.5281/zenodo.3786908
    """

    target_urls = {
        'speech': 'https://zenodo.org/api/files/765b45a3-c70d-48a6-936b-09a7989c349a/speech_f5e0d9f9.pth',
        'noise': 'https://zenodo.org/api/files/765b45a3-c70d-48a6-936b-09a7989c349a/noise_04a6fc2d.pth'
    }

    from model import OpenUnmix

    # determine the maximum bin count for a 16khz bandwidth model
    max_bin = utils.bandwidth_to_max_bin(
        rate=16000,
        n_fft=1024,
        bandwidth=16000
    )

    # load open unmix model
    unmix = OpenUnmix(
        n_fft=1024,
        n_hop=256,
        nb_channels=1,
        hidden_size=256,
        max_bin=max_bin
    )

    # enable centering of stft to minimize reconstruction error
    if pretrained:
        state_dict = torch.hub.load_state_dict_from_url(
            target_urls[target],
            map_location=device
        )
        unmix.load_state_dict(state_dict)
        unmix.stft.center = True
        unmix.eval()

    return unmix.to(device)


def umxhq(
    target='vocals', device='cpu', pretrained=True, *args, **kwargs
):
    """
    Open Unmix 2-channel/stereo BiLSTM Model trained on MUSDB18-HQ

    Args:
        target (str): select the target for the source to be separated.
                      Supported targets are
                        ['vocals', 'drums', 'bass', 'other']
        pretrained (bool): If True, returns a model pre-trained on MUSDB18-HQ
        device (str): selects device to be used for inference
    """
    # set urls for weights
    target_urls = {
        'bass': 'https://zenodo.org/api/files/1c8f83c5-33a5-4f59-b109-721fdd234875/bass-8d85a5bd.pth',
        'drums': 'https://zenodo.org/api/files/1c8f83c5-33a5-4f59-b109-721fdd234875/drums-9619578f.pth',
        'other': 'https://zenodo.org/api/files/1c8f83c5-33a5-4f59-b109-721fdd234875/other-b52fbbf7.pth',
        'vocals': 'https://zenodo.org/api/files/1c8f83c5-33a5-4f59-b109-721fdd234875/vocals-b62c91ce.pth'
    }

    from model import OpenUnmix

    # determine the maximum bin count for a 16khz bandwidth model
    max_bin = utils.bandwidth_to_max_bin(
        rate=44100,
        n_fft=4096,
        bandwidth=16000
    )

    # load open unmix model
    unmix = OpenUnmix(
        n_fft=4096,
        n_hop=1024,
        nb_channels=2,
        hidden_size=512,
        max_bin=max_bin
    )

    # enable centering of stft to minimize reconstruction error
    if pretrained:
        state_dict = torch.hub.load_state_dict_from_url(
            target_urls[target],
            map_location=device
        )
        unmix.load_state_dict(state_dict)
        unmix.stft.center = True
        unmix.eval()

    return unmix.to(device)


def umx(
    target='vocals', device='cpu', pretrained=True, *args, **kwargs
):
    """
    Open Unmix 2-channel/stereo BiLSTM Model trained on MUSDB18

    Args:
        target (str): select the target for the source to be separated.
                      Supported targets are
                        ['vocals', 'drums', 'bass', 'other']
        pretrained (bool): If True, returns a model pre-trained on MUSDB18-HQ
        device (str): selects device to be used for inference
    """
    # set urls for weights
    target_urls = {
        'bass': 'https://zenodo.org/api/files/d6105b95-8c52-430c-84ce-bd14b803faaf/bass-646024d3.pth',
        'drums': 'https://zenodo.org/api/files/d6105b95-8c52-430c-84ce-bd14b803faaf/drums-5a48008b.pth',
        'other': 'https://zenodo.org/api/files/d6105b95-8c52-430c-84ce-bd14b803faaf/other-f8e132cc.pth',
        'vocals': 'https://zenodo.org/api/files/d6105b95-8c52-430c-84ce-bd14b803faaf/vocals-c8df74a5.pth'
    }

    from model import OpenUnmix

    # determine the maximum bin count for a 16khz bandwidth model
    max_bin = utils.bandwidth_to_max_bin(
        rate=44100,
        n_fft=4096,
        bandwidth=16000
    )

    # load open unmix model
    unmix = OpenUnmix(
        n_fft=4096,
        n_hop=1024,
        nb_channels=2,
        hidden_size=512,
        max_bin=max_bin
    )

    # enable centering of stft to minimize reconstruction error
    if pretrained:
        state_dict = torch.hub.load_state_dict_from_url(
            target_urls[target],
            map_location=device
        )
        unmix.load_state_dict(state_dict)
        unmix.stft.center = True
        unmix.eval()

    return unmix.to(device)
