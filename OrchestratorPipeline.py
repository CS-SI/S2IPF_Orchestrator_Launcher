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

import json


class OrchestratorPipeline(object):

    def __init__(self, confjsonfile):
        self.conf_pipeline = None
        self.conf_file = confjsonfile
        with open(confjsonfile) as f:
            self.conf_pipeline = json.load(f)
        self.mode_idx = 0

    def get_skipped_pools(self, mode):
        for f in self.conf_pipeline["TASKTABLE_CONFIGURATION"]:
            if f["Name"] == mode :
                return f["SkippedPools"]
        return None

    def get_runned_pools(self, mode):
        for f in self.conf_pipeline["TASKTABLE_CONFIGURATION"]:
            if f["Name"] == mode:
                return f["RunnedPools"]
        return None

    def get_previous_mode(self, mode):
        for f in self.conf_pipeline["TASKTABLE_CONFIGURATION"]:
            if f["Name"] == mode:
                if "PreviousTask" in f :
                    if len(f["PreviousTask"]) > self.mode_idx:
                        current_idx = self.mode_idx
                        self.mode_idx += 1
                        return f["PreviousTask"][current_idx]
                    else:
                        return None
                else:
                    return None
        return None

    def has_previous_mode(self,mode):
        for f in self.conf_pipeline["TASKTABLE_CONFIGURATION"]:
            if f["Name"] == mode:
                if "PreviousTask" in f :
                    return True
                else:
                    return False
        return False

    def get_chain_name(self, mode):
        for f in self.conf_pipeline["TASKTABLE_CONFIGURATION"]:
            if f["Name"] == mode:
                return f["Chain"]
        return None

    def is_defined(self,mode):
        for f in self.conf_pipeline["TASKTABLE_CONFIGURATION"]:
            if f["Name"] == mode:
                return True
        return False

    def is_tasktable_step(self, mode):
        if mode in self.conf_pipeline["NO_TASKTABLE_STEPS"]:
            return False
        return True
