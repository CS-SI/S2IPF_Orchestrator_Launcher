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

import copy

from lxml import etree as et


class JobOrderOLQCHandler(object):

    def __init__(self, filename):
        self.tree_hdr = et.parse(filename)
        self.root_hdr = self.tree_hdr.getroot()
        self.filename = filename

    def set_processor_name(self, processor):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/Ipf_Conf/Processor_Name')
        result[0].text = processor

    def set_processor_version(self, version):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/Ipf_Conf/Version')
        result[0].text = version

    def set_log_level(self, level):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/Ipf_Conf/Stdout_Log_Level')
        result[0].text = level
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/Ipf_Conf/Stderr_Log_Level')
        result[0].text = level

    def set_processing_station(self, station):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/Ipf_Conf/Processing_Station')
        result[0].text = station

    def set_task_version(self, version):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/List_of_Ipf_Procs[1]/Ipf_Proc/Task_Version')
        result[0].text = version

    def set_safe_inputs(self, safes):
        base_xpath_filenames = '//Ipf_Job_Order/List_of_Ipf_Procs[1]/Ipf_Proc/List_of_Inputs/' \
                               'Input[File_Type/text()=\'PDI_SAFE\']/List_of_File_Names'
        list_of_filenames = self.root_hdr.xpath(base_xpath_filenames)
        filename_node_tpl = self.root_hdr.xpath(base_xpath_filenames + '[1]/File_Name')
        for g in safes:
            new_node = copy.deepcopy(filename_node_tpl[0])
            new_node.text = g
            list_of_filenames[0].append(new_node)
        list_of_filenames[0].remove(filename_node_tpl[0])
        list_of_filenames[0].attrib['count'] = str(len(safes))

    def set_gip_olqcpa_input(self, filename):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/List_of_Ipf_Procs[1]/Ipf_Proc/List_of_Inputs/Input[File_Type/'
            'text()=\'GIP_OLQCPA\']/List_of_File_Names[1]/File_Name')
        result[0].text = filename

    def set_gip_probas_input(self, filename):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/List_of_Ipf_Procs[1]/Ipf_Proc/List_of_Inputs/Input[File_Type/'
            'text()=\'GIP_PROBAS\']/List_of_File_Names[1]/File_Name')
        result[0].text = filename

    def set_working_input(self, filename):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/List_of_Ipf_Procs[1]/Ipf_Proc/List_of_Inputs/Input[File_Type/'
            'text()=\'WORKING\']/List_of_File_Names[1]/File_Name')
        result[0].text = filename

    def set_persistent_input(self, filename):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/List_of_Ipf_Procs[1]/Ipf_Proc/List_of_Inputs/Input[File_Type/'
            'text()=\'PERSISTENT_RESOURCES\']/List_of_File_Names[1]/File_Name')
        result[0].text = filename

    def set_idp_infos_input(self, filename):
        result = self.root_hdr.xpath(
            '//Ipf_Job_Order/List_of_Ipf_Procs[1]/Ipf_Proc/List_of_Inputs/Input[File_Type/'
            'text()=\'IDP_INFOS\']/List_of_File_Names[1]/File_Name')
        result[0].text = filename

    def set_output_report(self, filename):
        result = self.root_hdr.xpath('//Ipf_Job_Order/List_of_Ipf_Procs[1]/Ipf_Proc/List_of_Outputs/Output/File_Name')
        result[0].text = filename

    def write_to_file(self, filename):
        self.tree_hdr.write(filename, encoding="UTF-8")
