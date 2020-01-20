#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def start_server():
    from bert_base.server import BertServer
    from bert_base.server.helper import get_run_args

    args = get_run_args()
    print(args)
    server = BertServer(args)
    server.start()
    server.join()


if __name__ == '__main__':
    start_server()
