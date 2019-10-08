def checkModule (checklist, modulename):
  for name in checklist:
    if (name in modulename):
      return True
      
  return False

import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pygraphviz as pgv
import os

def header_opi(sinap_opi_path, afc_opi_path):
  out = '''<?xml version="1.0" encoding="UTF-8"?>
<display typeId="org.csstudio.opibuilder.Display" version="1.0.0">
  <actions hook="false" hook_all="false" />
  <auto_scale_widgets>
    <auto_scale_widgets>false</auto_scale_widgets>
    <min_width>-1</min_width>
    <min_height>-1</min_height>
  </auto_scale_widgets>
  <auto_zoom_to_fit_all>false</auto_zoom_to_fit_all>
  <background_color>
    <color red="240" green="240" blue="240" />
  </background_color>
  <boy_version>5.1.0.201711290101</boy_version>
  <foreground_color>
    <color red="192" green="192" blue="192" />
  </foreground_color>
  <grid_space>6</grid_space>
  <height>1000</height>
  <macros>
    <include_parent_macros>false</include_parent_macros>
  </macros>
  <name>Sirius Timing</name>
  <rules />
  <scripts />
  <show_close_button>true</show_close_button>
  <show_edit_range>true</show_edit_range>
  <show_grid>true</show_grid>
  <show_ruler>true</show_ruler>
  <snap_to_geometry>true</snap_to_geometry>
  <widget_type>connection</widget_type>
  <width>1000</width>
  <wuid>38e5eb62:14bffe23471:-789b</wuid>
  <x>-1</x>
  <y>-1</y>
  <widget typeId="org.csstudio.opibuilder.widgets.TextInput" version="2.0.0">
    <actions hook="false" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>'''+sinap_opi_path+'''EVG.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>$(text)</P>
          <R></R>
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <alarm_pulsing>false</alarm_pulsing>
    <auto_size>false</auto_size>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>3</border_style>
    <border_width>1</border_width>
    <confirm_message></confirm_message>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <format_type>0</format_type>
    <height>25</height>
    <horizontal_alignment>0</horizontal_alignment>
    <limits_from_pv>false</limits_from_pv>
    <maximum>1.7976931348623157E308</maximum>
    <minimum>-1.7976931348623157E308</minimum>
    <multiline_input>false</multiline_input>
    <name>Text Input</name>
    <precision>0</precision>
    <precision_from_pv>true</precision_from_pv>
    <pv_name>loc://EVG_P</pv_name>
    <pv_value />
    <rotation_angle>0.0</rotation_angle>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <selector_type>0</selector_type>
    <show_units>true</show_units>
    <style>0</style>
    <text></text>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <transparent>false</transparent>
    <visible>true</visible>
    <widget_type>Text Input</widget_type>
    <width>150</width>
    <wuid>49ef0909:166d9f978be:-1629</wuid>
    <x>18</x>
    <y>39</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.ActionButton" version="2.0.0">
    <actions hook="false" hook_all="true">
      <action type="OPEN_DISPLAY">
        <path>'''+sinap_opi_path+'''EVG.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <R></R>
          <P>$(text)</P>
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>40</height>
    <image></image>
    <name>Action Button_89</name>
    <push_action_index>0</push_action_index>
    <pv_name></pv_name>
    <pv_value />
    <rules>
      <rule name="Rule" prop_id="text" out_exp="true">
        <exp bool_exp="1">
          <value>pvStr0</value>
        </exp>
        <pv trig="true">loc://EVG_P</pv>
      </rule>
    </rules>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <style>1</style>
    <text>Generic-EVG</text>
    <toggle_button>false</toggle_button>
    <tooltip>P1916004</tooltip>
    <visible>true</visible>
    <widget_type>Action Button</widget_type>
    <width>150</width>
    <wuid>49ef0909:166d9f978be:6a16</wuid>
    <x>173</x>
    <y>32</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <actions hook="false" hook_all="false" />
    <auto_size>true</auto_size>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>17</height>
    <horizontal_alignment>1</horizontal_alignment>
    <name>Label_36</name>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <text>Generic EVG</text>
    <tooltip></tooltip>
    <transparent>true</transparent>
    <vertical_alignment>1</vertical_alignment>
    <visible>true</visible>
    <widget_type>Label</widget_type>
    <width>84</width>
    <wrap_words>false</wrap_words>
    <wuid>49ef0909:166d9f978be:733f</wuid>
    <x>51</x>
    <y>10</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.TextInput" version="2.0.0">
    <actions hook="false" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>'''+sinap_opi_path+'''EVG.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>$(text)</P>
          <R></R>
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <alarm_pulsing>false</alarm_pulsing>
    <auto_size>false</auto_size>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>3</border_style>
    <border_width>1</border_width>
    <confirm_message></confirm_message>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <format_type>0</format_type>
    <height>25</height>
    <horizontal_alignment>0</horizontal_alignment>
    <limits_from_pv>false</limits_from_pv>
    <maximum>1.7976931348623157E308</maximum>
    <minimum>-1.7976931348623157E308</minimum>
    <multiline_input>false</multiline_input>
    <name>Text Input_2</name>
    <precision>0</precision>
    <precision_from_pv>true</precision_from_pv>
    <pv_name>loc://EVRE_P</pv_name>
    <pv_value />
    <rotation_angle>0.0</rotation_angle>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <selector_type>0</selector_type>
    <show_units>true</show_units>
    <style>0</style>
    <text></text>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <transparent>false</transparent>
    <visible>true</visible>
    <widget_type>Text Input</widget_type>
    <width>150</width>
    <wuid>49ef0909:166d9f978be:73df</wuid>
    <x>18</x>
    <y>109</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.ActionButton" version="2.0.0">
    <actions hook="false" hook_all="true">
      <action type="OPEN_DISPLAY">
        <path>'''+sinap_opi_path+'''EVRE_Time_Units.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <R></R>
          <P>$(text)</P>
          <T></T>
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>40</height>
    <image></image>
    <name>Action Button_90</name>
    <push_action_index>0</push_action_index>
    <pv_name></pv_name>
    <pv_value />
    <rules>
      <rule name="Rule" prop_id="text" out_exp="true">
        <exp bool_exp="1">
          <value>pvStr0</value>
        </exp>
        <pv trig="true">loc://EVRE_P</pv>
      </rule>
    </rules>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <style>1</style>
    <text>Generic-EVR/EVE</text>
    <toggle_button>false</toggle_button>
    <tooltip>P1916004</tooltip>
    <visible>true</visible>
    <widget_type>Action Button</widget_type>
    <width>150</width>
    <wuid>49ef0909:166d9f978be:73e0</wuid>
    <x>173</x>
    <y>102</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <actions hook="false" hook_all="false" />
    <auto_size>true</auto_size>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>17</height>
    <horizontal_alignment>1</horizontal_alignment>
    <name>Label_37</name>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <text>Generic EVR/EVE</text>
    <tooltip></tooltip>
    <transparent>true</transparent>
    <vertical_alignment>1</vertical_alignment>
    <visible>true</visible>
    <widget_type>Label</widget_type>
    <width>117</width>
    <wrap_words>false</wrap_words>
    <wuid>49ef0909:166d9f978be:73e1</wuid>
    <x>34</x>
    <y>80</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.TextInput" version="2.0.0">
    <actions hook="false" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>'''+sinap_opi_path+'''EVG.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>$(text)</P>
          <R></R>
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <alarm_pulsing>false</alarm_pulsing>
    <auto_size>false</auto_size>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>3</border_style>
    <border_width>1</border_width>
    <confirm_message></confirm_message>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <format_type>0</format_type>
    <height>25</height>
    <horizontal_alignment>0</horizontal_alignment>
    <limits_from_pv>false</limits_from_pv>
    <maximum>1.7976931348623157E308</maximum>
    <minimum>-1.7976931348623157E308</minimum>
    <multiline_input>false</multiline_input>
    <name>Text Input_3</name>
    <precision>0</precision>
    <precision_from_pv>true</precision_from_pv>
    <pv_name>loc://FOUT_P</pv_name>
    <pv_value />
    <rotation_angle>0.0</rotation_angle>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <selector_type>0</selector_type>
    <show_units>true</show_units>
    <style>0</style>
    <text></text>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <transparent>false</transparent>
    <visible>true</visible>
    <widget_type>Text Input</widget_type>
    <width>150</width>
    <wuid>49ef0909:166d9f978be:73f7</wuid>
    <x>18</x>
    <y>179</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <actions hook="false" hook_all="false" />
    <auto_size>true</auto_size>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>17</height>
    <horizontal_alignment>1</horizontal_alignment>
    <name>Label_38</name>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <text>Generic Fout</text>
    <tooltip></tooltip>
    <transparent>true</transparent>
    <vertical_alignment>1</vertical_alignment>
    <visible>true</visible>
    <widget_type>Label</widget_type>
    <width>87</width>
    <wrap_words>false</wrap_words>
    <wuid>49ef0909:166d9f978be:73f9</wuid>
    <x>49</x>
    <y>150</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.ActionButton" version="2.0.0">
    <actions hook="false" hook_all="true">
      <action type="OPEN_DISPLAY">
        <path>'''+sinap_opi_path+'''FOUT.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <R></R>
          <P>$(text)</P>
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>40</height>
    <image></image>
    <name>Action Button_91</name>
    <push_action_index>0</push_action_index>
    <pv_name></pv_name>
    <pv_value />
    <rules>
      <rule name="Rule" prop_id="text" out_exp="true">
        <exp bool_exp="1">
          <value>pvStr0</value>
        </exp>
        <pv trig="true">loc://FOUT_P</pv>
      </rule>
    </rules>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <style>1</style>
    <text>Generic-Fout</text>
    <toggle_button>false</toggle_button>
    <tooltip>P1916004</tooltip>
    <visible>true</visible>
    <widget_type>Action Button</widget_type>
    <width>150</width>
    <wuid>49ef0909:166d9f978be:73f8</wuid>
    <x>173</x>
    <y>172</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.TextInput" version="2.0.0">
    <actions hook="false" hook_all="false">
      <action type="OPEN_DISPLAY">
        <path>'''+sinap_opi_path+'''EVG.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <P>$(text)</P>
          <R></R>
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <alarm_pulsing>false</alarm_pulsing>
    <auto_size>false</auto_size>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>3</border_style>
    <border_width>1</border_width>
    <confirm_message></confirm_message>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <format_type>0</format_type>
    <height>25</height>
    <horizontal_alignment>0</horizontal_alignment>
    <limits_from_pv>false</limits_from_pv>
    <maximum>1.7976931348623157E308</maximum>
    <minimum>-1.7976931348623157E308</minimum>
    <multiline_input>false</multiline_input>
    <name>Text Input_4</name>
    <precision>0</precision>
    <precision_from_pv>true</precision_from_pv>
    <pv_name>loc://AFC_P</pv_name>
    <pv_value />
    <rotation_angle>0.0</rotation_angle>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <selector_type>0</selector_type>
    <show_units>true</show_units>
    <style>0</style>
    <text></text>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <transparent>false</transparent>
    <visible>true</visible>
    <widget_type>Text Input</widget_type>
    <width>150</width>
    <wuid>7c4b6bab:169265dc59b:-6385</wuid>
    <x>18</x>
    <y>249</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.Label" version="1.0.0">
    <actions hook="false" hook_all="false" />
    <auto_size>true</auto_size>
    <background_color>
      <color red="255" green="255" blue="255" />
    </background_color>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>17</height>
    <horizontal_alignment>1</horizontal_alignment>
    <name>Label_39</name>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <text>Generic AFC</text>
    <tooltip></tooltip>
    <transparent>true</transparent>
    <vertical_alignment>1</vertical_alignment>
    <visible>true</visible>
    <widget_type>Label</widget_type>
    <width>82</width>
    <wrap_words>false</wrap_words>
    <wuid>7c4b6bab:169265dc59b:-6384</wuid>
    <x>52</x>
    <y>220</y>
  </widget>
  <widget typeId="org.csstudio.opibuilder.widgets.ActionButton" version="2.0.0">
    <actions hook="false" hook_all="true">
      <action type="OPEN_DISPLAY">
        <path>'''+afc_opi_path+'''AFC-EVR.opi</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <R></R>
          <P>$(text)</P>
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>40</height>
    <image></image>
    <name>Action Button_92</name>
    <push_action_index>0</push_action_index>
    <pv_name></pv_name>
    <pv_value />
    <rules>
      <rule name="Rule" prop_id="text" out_exp="true">
        <exp bool_exp="1">
          <value>pvStr0</value>
        </exp>
        <pv trig="true">loc://AFC_P</pv>
      </rule>
    </rules>
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <style>1</style>
    <text>Generic-AFC</text>
    <toggle_button>false</toggle_button>
    <tooltip>P1916004</tooltip>
    <visible>true</visible>
    <widget_type>Action Button</widget_type>
    <width>150</width>
    <wuid>7c4b6bab:169265dc59b:-6383</wuid>
    <x>173</x>
    <y>242</y>
  </widget>
'''

  return out
  
def end_opi():
  out = '</display>\n'
  
  return out

def button_opi(P, R, macros, opi_path, text, x, y, h, w, wuid):
  addmacros = ''
  for name in macros:
    value = macros[name]
    addmacros = addmacros + '<'+name+'>' + value + '</'+name+'>'+'\n'
    
  out = '''  <widget typeId="org.csstudio.opibuilder.widgets.ActionButton" version="2.0.0">
    <actions hook="false" hook_all="true">
      <action type="OPEN_DISPLAY">
        <path>''' + opi_path + '''</path>
        <macros>
          <include_parent_macros>true</include_parent_macros>
          <R>''' + R + '''</R>
          <P>''' + P + '''</P>
          ''' + addmacros + '''
        </macros>
        <mode>1</mode>
        <description></description>
      </action>
    </actions>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <height>''' + str(h) + '''</height>
    <image></image>
    <name>Action Button</name>
    <push_action_index>0</push_action_index>
    <pv_name></pv_name>
    <pv_value />
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <style>1</style>
    <text>''' + text + '''</text>
    <toggle_button>false</toggle_button>
    <tooltip></tooltip>
    <visible>true</visible>
    <widget_type>Action Button</widget_type>
    <width>''' + str(w) + '''</width>
    <wuid>''' + str(wuid) + '''</wuid>
    <x>''' + str(x) + '''</x>
    <y>''' + str(y) + '''</y>
  </widget>
'''
  return out
  
def text_opi_cluster(text, x, y, h, w, wuid):
  out = '''  <widget typeId="org.csstudio.opibuilder.widgets.TextUpdate" version="1.0.0">
    <actions hook="false" hook_all="true" />
    <alarm_pulsing>false</alarm_pulsing>
    <auto_size>false</auto_size>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color name="Dark Gray Border" red="190" green="190" blue="190" />
    </background_color>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="0" blue="0" />
    </border_color>
    <border_style>1</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="19" style="1" pixels="false">Header 1</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <format_type>0</format_type>
    <height>''' + str(h) + '''</height>
    <horizontal_alignment>1</horizontal_alignment>
    <name>Action Button</name>
    <precision>0</precision>
    <precision_from_pv>true</precision_from_pv>
    <pv_name></pv_name>
    <pv_value />
    <rotation_angle>0.0</rotation_angle>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <show_units>true</show_units>
    <text>''' + text + '''</text>
    <tooltip></tooltip>
    <transparent>true</transparent>
    <vertical_alignment>0</vertical_alignment>
    <visible>true</visible>
    <widget_type>Text Update</widget_type>
    <width>''' + str(w) + '''</width>
    <wrap_words>false</wrap_words>
    <wuid>''' + str(wuid) + '''</wuid>
    <x>''' + str(x) + '''</x>
    <y>''' + str(y) + '''</y>
  </widget>
'''
  return out
  
def text_opi(text, x, y, h, w, wuid):
  out = '''  <widget typeId="org.csstudio.opibuilder.widgets.TextUpdate" version="1.0.0">
    <actions hook="false" hook_all="true" />
    <alarm_pulsing>false</alarm_pulsing>
    <auto_size>false</auto_size>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color name="Dark Gray Border" red="190" green="190" blue="190" />
    </background_color>
    <border_alarm_sensitive>false</border_alarm_sensitive>
    <border_color>
      <color red="0" green="0" blue="0" />
    </border_color>
    <border_style>1</border_style>
    <border_width>1</border_width>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="0" green="0" blue="0" />
    </foreground_color>
    <format_type>0</format_type>
    <height>''' + str(h) + '''</height>
    <horizontal_alignment>1</horizontal_alignment>
    <name>Action Button</name>
    <precision>0</precision>
    <precision_from_pv>true</precision_from_pv>
    <pv_name></pv_name>
    <pv_value />
    <rotation_angle>0.0</rotation_angle>
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>false</keep_wh_ratio>
    </scale_options>
    <scripts />
    <show_units>true</show_units>
    <text>''' + text + '''</text>
    <tooltip></tooltip>
    <transparent>true</transparent>
    <vertical_alignment>0</vertical_alignment>
    <visible>true</visible>
    <widget_type>Text Update</widget_type>
    <width>''' + str(w) + '''</width>
    <wrap_words>false</wrap_words>
    <wuid>''' + str(wuid) + '''</wuid>
    <x>''' + str(x) + '''</x>
    <y>''' + str(y) + '''</y>
  </widget>
'''
  return out
  
def led_opi(P, R, pvName, x, y, h, w, wuid):
  out = '''  <widget typeId="org.csstudio.opibuilder.widgets.LED" version="1.0.0">
    <actions hook="false" hook_all="false" />
    <alarm_pulsing>false</alarm_pulsing>
    <backcolor_alarm_sensitive>false</backcolor_alarm_sensitive>
    <background_color>
      <color red="240" green="240" blue="240" />
    </background_color>
    <bit>-1</bit>
    <border_alarm_sensitive>true</border_alarm_sensitive>
    <border_color>
      <color red="0" green="128" blue="255" />
    </border_color>
    <border_style>0</border_style>
    <border_width>1</border_width>
    <bulb_border>3</bulb_border>
    <bulb_border_color>
      <color red="150" green="150" blue="150" />
    </bulb_border_color>
    <data_type>0</data_type>
    <effect_3d>true</effect_3d>
    <enabled>true</enabled>
    <font>
      <opifont.name fontName="Ubuntu" height="11" style="0" pixels="false">Default</opifont.name>
    </font>
    <forecolor_alarm_sensitive>false</forecolor_alarm_sensitive>
    <foreground_color>
      <color red="192" green="192" blue="192" />
    </foreground_color>
    <height>''' + str(h) + '''</height>
    <name>LED_31</name>
    <off_color>
      <color red="255" green="0" blue="0" />
    </off_color>
    <off_label>OFF</off_label>
    <on_color>
      <color red="0" green="255" blue="0" />
    </on_color>
    <on_label>ON</on_label>
    <pv_name>''' + P + R + pvName + '''</pv_name>
    <pv_value />
    <rules />
    <scale_options>
      <width_scalable>true</width_scalable>
      <height_scalable>true</height_scalable>
      <keep_wh_ratio>true</keep_wh_ratio>
    </scale_options>
    <scripts />
    <show_boolean_label>false</show_boolean_label>
    <square_led>false</square_led>
    <tooltip>$(pv_name)
$(pv_value)</tooltip>
    <visible>true</visible>
    <widget_type>LED</widget_type>
    <width>''' + str(w) + '''</width>
    <wuid>''' + str(wuid) + '''</wuid>
    <x>''' + str(x) + '''</x>
    <y>''' + str(y) + '''</y>
  </widget>
  '''
  return out

def connection_opi(arrows, r, g, b, src_wuid, tgt_wuid, wuid):
  out = '''  <connection typeId="org.csstudio.opibuilder.connection" version="1.0.0">
    <anti_alias>true</anti_alias>
    <arrow_length>20</arrow_length>
    <arrows>''' + str(arrows) + '''</arrows>
    <fill_arrow>true</fill_arrow>
    <line_color>
      <color red="''' + str(r) + '''" green="''' + str(g) + '''" blue="''' + str(b) + '''" />
    </line_color>
    <line_jump_add>0</line_jump_add>
    <line_jump_size>10</line_jump_size>
    <line_jump_style>0</line_jump_style>
    <line_style>0</line_style>
    <line_width>2</line_width>
    <name>connection</name>
    <points />
    <router>0</router>
    <src_path></src_path>
    <src_term>RIGHT</src_term>
    <src_wuid>''' + str(src_wuid) + '''</src_wuid>
    <tgt_path></tgt_path>
    <tgt_term>LEFT</tgt_term>
    <tgt_wuid>''' + str(tgt_wuid) + '''</tgt_wuid>
    <widget_type>connection</widget_type>
    <wuid>''' + str(wuid) + '''</wuid>
  </connection>
'''
  return out

def color2rgb (color_name):
  color_dic = {}
  color_dic['limegreen'] = [0,200,0]
  color_dic['blue'] = [0,0,255]
  color_dic['red'] = [255,0,0]
  color_dic['purple'] = [200,0,255]
  if (color_name in color_dic):
    return color_dic[color_name]
  else:
    return [0,0,0]

def has_nodeSubgraph (subgraphList, node):
  for sub in subgraphList:
    if (subgraphList[sub].has_node(node)):
      return True
  return False

opi_file = open('../op/opi/sirius_main_timing.opi','w')
sinap_opi_path = 'sinap-timing-epics-ioc/'
afc_opi_path = 'tim-rx-epics-ioc/'

# Load graphviz layout
# A=pgv.AGraph("Timing_Network.dot")
# A_opi=pgv.AGraph("Timing_Network_OPI.dot")

A=pgv.AGraph(strict=False,directed=True,compound=True,landscape=False,ranksep='equally',rankdir='LR',splines='true')
A.node_attr['shape']='box'
A.node_attr['style']='rounded'
A.node_attr['fontsize']='32'
A.node_attr['penwidth']='3'
A.node_attr['width']='7'
A.edge_attr['penwidth']=3
A.edge_attr['fontsize']='24'
A.graph_attr['label']='Timing System Network'
A.graph_attr['fontsize']='50'

remote_data = True

if (remote_data):
  # Setup the Sheets API
  SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

  creds = None
  # The file token.pickle stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
      creds = pickle.load(token)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json', SCOPES)
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
      pickle.dump(creds, token)

  service = build('sheets', 'v4', credentials=creds)
  
  # Call the Sheets API
  SPREADSHEET_ID = '19lNNPWxZJv5s-VTrwZRMNWLDMqdHzOQa3ZDIw5neYFI'
  RANGE_NAME = 'Cabos e Fibras'
  print('Loading remote data...')
  result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
  values = result.get('values', [])
  print('Loaded', RANGE_NAME)

else:
  print('Loading local data...')
  values = csv2list ('Cabos_e_Fibras_Sirius.csv')

#Filters
HideFiberPatchs = 1
HidePassiveModules = 1

FiberPatchName = 'DIO'
ActiveModules = ['EVG', 'Fout', 'EVR', 'EVE', FiberPatchName]
OEModules = ['OE', 'OERF']

SistemaFilter = []
SistemaFilter = SistemaFilter + ['Timing']
SistemaFilter = SistemaFilter + ['Timing Fontes']
SistemaFilter = SistemaFilter + ['Timing Diagnostico']
SistemaFilter = SistemaFilter + ['Timing Linac']
SistemaFilter = SistemaFilter + ['Timing AFC']
SistemaFilter = SistemaFilter + ['Timing Pulsados']
SistemaFilter = SistemaFilter + ['Timing RF']
SistemaFilter = SistemaFilter + ['Controle']

dict_subgraphs = {}

for name in SistemaFilter[1:-1]:
  dict_subgraphs[name] = A.add_subgraph([], name = 'cluster_'+name.replace(' ',''))
  dict_subgraphs[name].graph_attr['shape']='box'
  dict_subgraphs[name].graph_attr['style']='rounded'
  dict_subgraphs[name].graph_attr['label']=name
  dict_subgraphs[name].graph_attr['fontsize']='50'
  dict_subgraphs[name].graph_attr['rank']='same'
  dict_subgraphs[name].graph_attr['margin']='50,50'

if not values:
    print('No data found.')
else:
    header = {}
    tableline = [0]
    for i in range(len(values[0])):
      header[values[0][i]] = i
    # print (header)
    sheetWidth = len(header)
    #for i in values:
    for n in range(len(values)):
      i = values[n]

      # SistemaFilter
      if (i[header['Sistema']] in SistemaFilter):
        True
      else:
        continue
      
      # Filter to hide passive modules
      if (HidePassiveModules == 1):
        if (any(word in i[header['Equipamento 1']] for word in ActiveModules) & any(word in i[header['Equipamento 2']] for word in ActiveModules)):
          True
        else:
          continue
      
      # Port name and network edge direction
      if ('OUT' in i[header['Porta 1']].upper()) | ('OTP' in i[header['Porta 1']].upper()) | ('IN' in i[header['Porta 2']].upper()) | ('OE' in i[header['Porta 2']].upper()) | ('TX' in i[header['Equipamento 1']].upper()):
        dev_u = i[header['Equipamento 1']]
        port_u = i[header['Porta 1']]
        local_u = i[header['Local 1']]
        dev_v = i[header['Equipamento 2']]
        port_v = i[header['Porta 2']]
        local_v = i[header['Local 2']]
        #print (dev_u, dev_v)
      elif ((i[header['Porta 1']].upper() == i[header['Porta 2']].upper()) & (FiberPatchName in i[header['Equipamento 1']])):
        dev_u = i[header['Equipamento 1']]
        port_u = i[header['Porta 1']]
        local_u = i[header['Local 1']]
        dev_v = i[header['Equipamento 2']]
        port_v = i[header['Porta 2']]
        local_v = i[header['Local 2']]
        #print ('***',dev_u, dev_v)
      else:
        dev_u = i[header['Equipamento 2']]
        port_u = i[header['Porta 2']]
        local_u = i[header['Local 2']]
        dev_v = i[header['Equipamento 1']]
        port_v = i[header['Porta 1']]
        local_v = i[header['Local 1']]
        #print (dev_u, dev_v)

      if (FiberPatchName in dev_u):
        dev_u = dev_u+port_u
      else:
        dev_u = dev_u+'\n'+local_u

      if (FiberPatchName in dev_v):
        dev_v = dev_v+port_v
      else:
        dev_v = dev_v+'\n'+local_v

      # Graph or subgraph
      if (i[header['Sistema']] in dict_subgraphs):
        #dict_subgraphs[i[header['Sistema']]].add_edge(dev_u,dev_v)
        if (has_nodeSubgraph(dict_subgraphs, dev_u) == False):
          dict_subgraphs[i[header['Sistema']]].add_node(dev_u)
        if (has_nodeSubgraph(dict_subgraphs, dev_v) == False):
          dict_subgraphs[i[header['Sistema']]].add_node(dev_v)
      else:
        if (local_u in dict_subgraphs):
          dict_subgraphs[local_u].add_node(dev_u)
        if (local_v in dict_subgraphs):
          dict_subgraphs[local_v].add_node(dev_v)

      A.add_edge(dev_u,dev_v)
      e = A.get_edge(dev_u,dev_v)

      # edge color filter
      if ('1 MM' in i[header['Tipo de Cabo/Fibra']].upper()):
        e.attr['color'] = 'limegreen'
        e.attr['style'] = 'dashed'
      elif ('OM4' in i[header['Tipo de Cabo/Fibra']].upper()):
        e.attr['color'] = 'blue'
        e.attr['style'] = 'solid'
      elif ('MONOMODO' in i[header['Tipo de Cabo/Fibra']].upper()):
        e.attr['color'] = 'purple'
        e.attr['style'] = 'bold'
      else:
        e.attr['color'] = 'red'
        e.attr['style'] = 'dotted'
        
      # edge count to label
      e.attr['portOut'] = port_u
      e.attr['portIn'] = port_v
      if (FiberPatchName in dev_v) | (FiberPatchName in dev_u):
        e.attr['label'] = e.attr['portOut']+' to '+e.attr['portIn']+'\n'+'Len: '+i[header['Comprimento arredondado[m]']]+'m'+'\n'+i[header['Label']]
      else:
        e.attr['label'] = i[header['Conector 1']]+' to '+i[header['Conector 2']]+'\t'+'Len: '+i[header['Comprimento arredondado[m]']]+'m'+'\n'+i[header['Label']]
      
      # Store table line to generate a filtered table
      tableline = tableline + [n]

# Hide Fiber Patch connections
if (HideFiberPatchs == 1):
  for node in A.nodes():
    if (FiberPatchName in node):
      nbr = A[node]
      if (len(nbr) > 2):
        print ('Warning: FibPatch with more than 2 connections', node, nbr)
      if (len(nbr) == 2):
        try:
          e0 = A.get_edge(node,nbr[0])
        except:
          e0 = A.get_edge(nbr[0],node)
        try:
          e1 = A.get_edge(nbr[1],node)
        except:
          e1 = A.get_edge(node,nbr[1])
        if ('OUT' in e0.attr['portOut'].upper()):
          A.add_edge(nbr[0],nbr[1],color=e0.attr['color'],portOut=e0.attr['portOut'],portIn=e1.attr['portIn'],label=e0.attr['portOut']+' to '+e1.attr['portIn']+'\n'+FiberPatchName)
        else:
          A.add_edge(nbr[1],nbr[0],color=e0.attr['color'],portOut=e1.attr['portOut'],portIn=e0.attr['portIn'],label=e1.attr['portOut']+' to '+e0.attr['portIn']+'\n'+FiberPatchName)
      A.remove_node(node)

# Exclude unconncted Fiber Patchs 
for node in A.nodes():
  if (FiberPatchName in node):
    nbr = A[node]
    if (len(nbr) < 2):
      A.remove_node(node)

A.layout(prog='dot') # layout with dot options: neato|dot|twopi|circo|fdp|nop

opi = ''

opi = opi + header_opi(sinap_opi_path, afc_opi_path)

height = 30
width = 230
scaleX = 1.75
scaleY = 1.75

wuid = 1
wuid_dic = {}

########################### Drawing Nodes ##############################
ymax = float(A.graph_attr['bb'].split(',')[3])

# drawing clusters
for G in A.subgraphs():
  if ('Legend' in G.graph_attr['label']):
    continue
  [xi,yi,xf,yf] = list(map(float, G.graph_attr['bb'].split(',')))
  x = xi / scaleX
  y = (ymax - yf) / scaleY
  w = (xf-xi) / scaleX
  h = (yf-yi) / scaleY
  opi = opi + text_opi_cluster(G.graph_attr['label'].replace('&','&amp;'), x, y, h, w, wuid)
  wuid = wuid + 1

#drawing nodes
for node in A.nodes():
  if (('TI' in node) & (node in A)):
    width = float(node.attr['width'])*33
    
    # define name and position
    node_opi = A.get_node(node)
    name = node_opi.split('\n')[0]
    location = node_opi.split('\n')[1]
    wuid_dic[name] = wuid
    P = name.split(':')[0] + ':'
    R = name.split(':')[1] + ':'
    label = P + R
    pos = node_opi.attr['pos']
    x = float(pos.split(',')[0]) / scaleX
    y = (ymax - float(pos.split(',')[1]) - height) / scaleY
    
    # define widget type
    if ('-Fout' in node_opi):
      opi_path = sinap_opi_path+'FOUT.opi'
      module = 'FOUT'
    elif ('-EVG' in node_opi):
      opi_path = sinap_opi_path+'EVG.opi'
      module = 'EVG'
    elif ('-EVR' in node_opi):
      opi_path = sinap_opi_path+'EVRE_Time_Units.opi'
      module = 'EVR'
    elif ('-EVE' in node_opi):
      opi_path = sinap_opi_path+'EVRE_Time_Units.opi'
      module = 'EVE'
    elif ('AMC' in node_opi):
      opi_path = afc_opi_path+'AFC-EVR.opi'
      module = 'AMC'
    else:
      opi = opi + text_opi(label, x, y, height, width, wuid)
      wuid = wuid + 1
      continue
    
    # define OTP and OUT macros 
    macros = {}
    for edge in A.edges(node):
      for i in range(24):
        if not(('OTP'+str(i)) in macros):
          macros['OTP'+str(i)] = 'Disconnected'
        if (('OTP'+str(i)) in edge.attr['portOut']) & (P[0:-1] in edge[0]) & (R[0:-1] in edge[0]):
          macros['OTP'+str(i)] = edge[1].split('\n')[0] + '\n' + edge.attr['portIn']
          print (edge, edge.attr['portOut'])
      for i in range(8):
        if not(('OUT'+str(i)) in macros):
          macros['OUT'+str(i)] = 'Disconnected'
        if (('OUT'+str(i)) in edge.attr['portOut']) & (P[0:-1] in edge[0]) & (R[0:-1] in edge[0]):
          macros['OUT'+str(i)] = edge[1].split('\n')[0] + '\n' + edge.attr['portIn']
          macros['OTP'+str(i+12)] = edge[1].split('\n')[0] + '\n' + edge.attr['portIn']
          print (edge, edge.attr['portOut'])
    
    x = x - width/2
    macros['T'] = ''
    opi = opi + button_opi(P, R, macros, opi_path, label, x, y, height, width, wuid)
    wuid = wuid + 1
    
    if (module == 'EVR') | (module == 'EVE') | (module == 'AMC'):
      macros['T'] = 'Raw'
      opi = opi + button_opi(P, R, macros, opi_path, 'Raw', x+width+1, y, height, 50, wuid)
      wuid = wuid + 1
    
    # Link or RF Status LED
    if (module == 'EVG'):
      opi = opi + text_opi('RF In', x, y+height+1, 20, width/4, wuid)
      wuid = wuid + 1
      
      opi = opi + led_opi(P, R, 'RFStatus-Mon', x+width/4+5, y+height+1, 20, 20, wuid)
      wuid = wuid + 1
    
    else:
      opi = opi + text_opi('Link', x, y+height+1, 20, width/4, wuid)
      wuid = wuid + 1
      
      opi = opi + led_opi(P, R, 'LinkStatus-Mon', x+width/4+5, y+height+1, 20, 20, wuid)
      wuid = wuid + 1
    
    # Network or Reference clock lock status
    if (module == 'AMC'):
      opi = opi + text_opi('Ref Clock', x+width/2, y+height+1, 20, width/3, wuid)
      wuid = wuid + 1
      
      opi = opi + led_opi(P, R, 'RefClkLocked-Mon', x+width/2+width/3+5, y+height+1, 20, 20, wuid)
      wuid = wuid + 1
  
    else:
      opi = opi + text_opi('Network', x+width/2, y+height+1, 20, width/3, wuid)
      wuid = wuid + 1
      
      opi = opi + led_opi(P, R, 'Network-Mon', x+width/2+width/3+5, y+height+1, 20, 20, wuid)
      wuid = wuid + 1
  
# drawing connections
for edge in A.edges():
  node0 = edge[0].split('\n')[0]
  node1 = edge[1].split('\n')[0]
  if ((node0 in wuid_dic) & (node1 in wuid_dic)):
    [r,g,b] = color2rgb(edge.attr['color'])
    opi = opi + connection_opi(2, r, g, b, wuid_dic[node0], wuid_dic[node1], wuid)
    wuid = wuid + 1

opi = opi + end_opi()

opi_file.write(opi)

opi_file.close()
  
      
##################### Debug ############################
A.draw('sirius_main_timing.pdf') # draw pdf
