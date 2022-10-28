# coding=utf-8
#  Copyright (C) 2020-2022 CS GROUP – France, https://www.csgroup.eu
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# author : Esquis Benjamin for CSGroup
#

import logging

PROCESSING_STATION = "2BPS"
VERSION = "1.0.0"
PROCESSOR_LOG_LEVEL = "DEBUG"

IDPSC_EXE_DIR = "/dpc/app/s2ipf"
DEFAULT_SENSING_START = "1983-01-01T00:00:00Z"
DEFAULT_SENSING_STOP = "2020-01-01T00:00:00Z"
DEFAULT_SENSING_START_MS = "1983-01-01T00:00:00.000Z"
DEFAULT_SENSING_STOP_MS = "2020-01-01T00:00:00.000Z"
DEFAULT_NB_TASKS = 4
DEFAULT_AQUISITION_STATION = ""
DEFAULT_PROCESSOR_NAME = "Chain"
DEFAULT_DETECTOR_LIST = "01-02-03-04-05-06-07-08-09-10-11-12"
DEFAULT_BAND_LIST = "B00-B01-B02-B03-B04-B05-B06-B07-B08-B09-B10-B11-B12"
NO_B00_BAND_LIST = "B01-B02-B03-B04-B05-B06-B07-B08-B09-B10-B11-B12"
ONLY_B00_BAND_LIST = "B00"
ONLY_D01_DETECTOR_LIST = "01"


LOG_FORMATTER=logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s : %(message)s', "%Y-%m-%d %H:%M:%S")
