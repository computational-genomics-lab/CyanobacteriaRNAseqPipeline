#!/usr/bin/env python3
import luigi
import sys


from tasks.readCleaning.rawReadQC import readqc
from tasks.readCleaning.rawReadQC import rawReadsQC
from tasks.readCleaning.preProcessReads import bbduk
from tasks.readCleaning.preProcessReads import cleanReads
from tasks.readCleaning.reFormatReads import reformat


#ALIGNMENT FREE
from tasks.rnaSeq.alignmentFree import indexTransctriptome
from tasks.rnaSeq.alignmentFree import generate_transcript_count_file
from tasks.rnaSeq.alignmentFree import alignment_free_differential_expression_analysis


#ALIGNMENT BASED 

from tasks.rnaSeq.annotation import prokaryotic_annotation
from tasks.rnaSeq.annotation import make_tx_to_gene



if __name__ == '__main__':

    luigi.run()
