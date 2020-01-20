import sys
import os
import shutil

from bert_base.train.conlleval import metrics, evaluate, ANY_SPACE
from bert_base.train.train_helper import get_args_parser
from bert_base.train.bert_lstm_ner import train

ROOT_DIR = './BERT-BiLSTM-CRF-NER'


def train_ner():
    args = get_args_parser()
    if True:
        import sys
        param_str = '\n'.join(['%20s = %s' % (k, v)
                               for k, v in sorted(vars(args).items())])
        print('usage: %s\n%20s   %s\n%s\n%s\n' %
              (' '.join(sys.argv), 'ARG', 'VALUE', '_' * 50, param_str))
    print(args)
    os.environ['CUDA_VISIBLE_DEVICES'] = args.device_map
    train(args=args)


def is_better(baseline_counts, eval_counts, threshold=0.01):

    baseline_overall, _ = metrics(baseline_counts)
    eval_overall, _ = metrics(eval_counts)

    if (eval_overall.fscore - baseline_overall.fscore) < threshold:
        return False
    return True


def parse_args(argv):
    import argparse
    parser = argparse.ArgumentParser(
        description='evaluate tagging results using CoNLL criteria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    arg = parser.add_argument
    arg('-b', '--boundary', metavar='STR', default='-X-',
        help='sentence boundary')
    arg('-d', '--delimiter', metavar='CHAR', default=ANY_SPACE,
        help='character delimiting items in input')
    arg('-o', '--otag', metavar='CHAR', default='O',
        help='alternative outside tag')
    arg('file', nargs='?', default=None)
    return parser.parse_args(argv)


def eval(baseline_file, eval_file):
    with open(baseline_file) as f:
        baseline_counts = evaluate(f)

    with open(eval_file) as f:
        eval_counts = evaluate(f)

    if not is_better(baseline_counts, eval_counts):
        sys.exit('Baseline model is better, stop CI.')
    else:
        shutil.move(ROOT_DIR + '/baseline', ROOT_DIR + '/models/old-version')
        shutil.move(ROOT_DIR + '/output', ROOT_DIR + '/baseline')


if __name__ == '__main__':
    train_ner()
    baseline_file = ROOT_DIR + '/baseline/label_test.txt'
    eval_file = ROOT_DIR + '/output/label_test.txt'
    if os.path.exists(baseline_file) and os.path.exists(eval_file):
        eval(baseline_file, eval_file)
