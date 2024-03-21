import apache_beam as beam
import re
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

import argparse
import logging
import re

#inputs_pattern = 'data/SMSSpamCollection'
#outputs_prefix_ham = 'outputs/fullcodeham'
outputs_prefix_spam = 'outputs/fullcodespam'

def run(argv=None, save_main_session=True):
    """Main entry point; defines and runs the wordcount pipeline."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        default='gs://demo-gcp/source/SMSSpamCollection',
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        required=True,
        help='Output file to write results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session

    # Spam Word Count
    with beam.Pipeline(options=pipeline_options) as pipeline1:
        spam = (
            pipeline1
                | 'Take in Dataset' >> beam.io.ReadFromText(known_args.input)
                | 'Separate to list' >> beam.Map(lambda line: line.split("\t"))
                | 'Filter out only spam' >> beam.Filter(lambda line: line[0] == "spam")
                | 'Find words' >> beam.FlatMap(lambda line: re.findall(r"[a-zA-Z']+", line[1]))
                | 'Pair words with 1' >> beam.Map(lambda word: (word, 1))
                | 'Group and sum' >> beam.CombinePerKey(sum)
                | 'Format results' >> beam.Map(lambda word_c: str(word_c))
                | 'Write results' >> beam.io.WriteToText(known_args.output, file_name_suffix = ".txt")
                )


if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()