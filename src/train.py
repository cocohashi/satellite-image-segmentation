import logging
import torch

from pathlib import Path
from torch.utils.data import DataLoader, random_split

from utils.data_loading import BasicDataset, AerialDataset


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

dir_img = Path('../data/dataset/semantic_drone_dataset/original_images/')
dir_mask = Path('../data//dataset/semantic_drone_dataset/label_images_semantic/')

def train(img_scale: float = 0.5,
            val_percent: float = 0.1,
            batch_size: int = 1):
    try:
        dataset = AerialDataset(dir_img, dir_mask, img_scale)
    except (AssertionError, RuntimeError):
        dataset = BasicDataset(dir_img, dir_mask, img_scale)

    # 2. Split into train / validation partitions
    n_val = int(len(dataset) * val_percent)
    n_train = len(dataset) - n_val
    train_set, val_set = random_split(dataset, [n_train, n_val], generator=torch.Generator().manual_seed(0))

    # 3. Create data loaders
    loader_args = dict(batch_size=batch_size, num_workers=4, pin_memory=True)
    train_loader = DataLoader(train_set, shuffle=True, **loader_args)
    val_loader = DataLoader(val_set, shuffle=False, drop_last=True, **loader_args)

    return None

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    logger.info(f'Using device {device}')

    try:
        train()
    except KeyboardInterrupt:
        # torch.save(net.state_dict(), 'INTERRUPTED.pth')
        logger.info('Saved interrupt')
        raise