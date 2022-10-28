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

from lxml import etree as ET


class TaskTableReader(object):

    def __init__(self, filename):
        self.tree_hdr = ET.parse(filename)
        self.root_hdr = self.tree_hdr.getroot()
        self.filename = filename

    def replace_pool_count(self, newcount):
        """

        """
        pool_list = self.root_hdr.find("List_of_Pools")
        pool_list.attrib["count"] = str(newcount)

    def set_fake_mode(self, fakemode=True):
        """
            set fake mode
        """
        test_node = self.root_hdr.find("Test")
        if fakemode:
            test_node.text = "true"
        else:
            test_node.text = "false"

    def set_IDPSCs_versions(self, json_versions):
        #get all the Tasks
        task_nodes = self.root_hdr.findall("./List_of_Pools/Pool/List_of_Tasks/Task")
        for f in task_nodes:
            task_name =f.find("Name").text
            if task_name.startswith("OLQC"):
                task_name = "OLQC"
            if not task_name in json_versions:
                raise Exception("No "+task_name+" defined in IDPSC_EXE_export for this chain ")
            f.find("Version").text = json_versions[task_name]

    def write_to_file(self):
        self.tree_hdr.write(self.filename)
