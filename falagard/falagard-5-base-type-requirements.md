<a id="fal_baseclass_ref"></a>
# CEGUI Widget Base Type Requirements

> CEGUI 0.8.7 · Falagard skinning system · converted from [`fal_baseclass_ref.dox`](https://github.com/cegui/cegui/blob/v0-8-7/doc/doxygen/falagard/fal_baseclass_ref.dox) ([original page](https://static.cegui.org.uk/docs/0.8.7/fal_baseclass_ref.html)). Text unchanged; format only.

The following is a reference to the required elements in a WidgetLook as dictated by the widget base classes available within CEGUI.  We also state the recommended window renderer to be mapped from the FalagardWRBase module, though you are free to use a custom window renderer as your needs dictate.

<a id="fal_baseclass_ref_sec_0"></a>
## Section Contents

- [DefaultWindow](#fal_baseclass_ref_sec_1)
- [CEGUI/Checkbox](#fal_baseclass_ref_sec_2)
- [CEGUI/ComboDropList](#fal_baseclass_ref_sec_3)
- [CEGUI/Combobox](#fal_baseclass_ref_sec_4)
- [CEGUI/DragContainer](#fal_baseclass_ref_sec_5)
- [CEGUI/Editbox](#fal_baseclass_ref_sec_6)
- [CEGUI/FrameWindow](#fal_baseclass_ref_sec_7)
- [CEGUI/ItemEntry](#fal_baseclass_ref_sec_8)
- [CEGUI/ItemListbox](#fal_baseclass_ref_sec_9)
- [CEGUI/ListHeader](#fal_baseclass_ref_sec_10)
- [CEGUI/ListHeaderSegment](#fal_baseclass_ref_sec_11)
- [CEGUI/Listbox](#fal_baseclass_ref_sec_12)
- [CEGUI/MenuItem](#fal_baseclass_ref_sec_13)
- [CEGUI/Menubar](#fal_baseclass_ref_sec_14)
- [CEGUI/MultiColumnList](#fal_baseclass_ref_sec_15)
- [CEGUI/MultiLineEditbox](#fal_baseclass_ref_sec_16)
- [CEGUI/PopupMenu](#fal_baseclass_ref_sec_17)
- [CEGUI/ProgressBar](#fal_baseclass_ref_sec_18)
- [CEGUI/PushButton](#fal_baseclass_ref_sec_19)
- [CEGUI/RadioButton](#fal_baseclass_ref_sec_20)
- [CEGUI/ScrollablePane](#fal_baseclass_ref_sec_21)
- [CEGUI/Scrollbar](#fal_baseclass_ref_sec_22)
- [CEGUI/Slider](#fal_baseclass_ref_sec_23)
- [CEGUI/Spinner](#fal_baseclass_ref_sec_24)
- [CEGUI/TabButton](#fal_baseclass_ref_sec_25)
- [CEGUI/TabControl](#fal_baseclass_ref_sec_26)
- [CEGUI/Thumb](#fal_baseclass_ref_sec_27)
- [CEGUI/Titlebar](#fal_baseclass_ref_sec_28)
- [CEGUI/Tooltip](#fal_baseclass_ref_sec_29)
- [CEGUI/Tree](#fal_baseclass_ref_sec_30)

<a id="fal_baseclass_ref_sec_1"></a>
## DefaultWindow

Base class intended to be used as a simple, generic container window.  The logic for this class does nothing.

You should use a "Core/Default" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_2"></a>
## CEGUI/Checkbox

Base class providing logic for Checkbox / toggle button widgets.

You should use a "Core/ToggleButton" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_3"></a>
## CEGUI/ComboDropList

Base class providing logic for the combo box drop down list sub-widget.  This is a specialisation of the "CEGUI/Listbox" class.

You should use a "Core/Listbox" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Scrollbar based widget with name suffix "__auto_vscrollbar__". This widget will be used to control vertical scroll position.
  - Scrollbar based widget with name suffix "__auto_hscrollbar__". This widget will be used to control horizontal scroll position.

<a id="fal_baseclass_ref_sec_4"></a>
## CEGUI/Combobox

Base class providing logic for the combo box widget.

You should use a "Core/Default" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Editbox based widget with name suffix "__auto_editbox__"
  - ComboDropList based widget with name suffix "__auto_droplist__"
  - PushButton based widget with name suffix "__auto_button__"

<a id="fal_baseclass_ref_sec_5"></a>
## CEGUI/DragContainer

Base class providing logic for a generic container that supports drag and drop.

You should use a "Core/Default" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_6"></a>
## CEGUI/Editbox

Base class providing logic for a basic, single line, editbox / textbox widget.

You should use a "Core/Editbox" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_7"></a>
## CEGUI/FrameWindow

Base class providing logic for a window that is movable, sizable, and has a title-bar, frame, and a close button.

You should use a "Core/FrameWindow" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Titlebar based widget with name suffix "__auto_titlebar__". This widget will be used as the title bar for the frame window.
  - PushButton based widget with name suffix "__auto_closebutton__". This widget will be used as the close button for the frame window.

<a id="fal_baseclass_ref_sec_8"></a>
## CEGUI/ItemEntry

Base class providing logic for entries in supporting list widgets such as ItemListbox.

You should use a "Core/ItemEntry" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_9"></a>
## CEGUI/ItemListbox

Base class providing logic for a listbox widget that is able to use ItemEntry based windows as items in the list.

You should use a "Core/ItemListbox" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Scrollbar based widget with name suffix "__auto_vscrollbar__". This widget will be used to control vertical scroll position.
  - Scrollbar based widget with name suffix "__auto_hscrollbar__". This widget will be used to control horizontal scroll position.

<a id="fal_baseclass_ref_sec_10"></a>
## CEGUI/ListHeader

Base class providing logic for a multi columned header widget - intended for use on the multi column list.

You should use a "Core/ListHeader" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_11"></a>
## CEGUI/ListHeaderSegment

Base class providing logic for a widget representing single segment / column of the ListHeader widget.

You should use a "Core/ListHeaderSegment" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_12"></a>
## CEGUI/Listbox

Base class providing logic for a simple single column list widget.

You should use a "Core/Listbox" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Scrollbar based widget with name suffix "__auto_vscrollbar__". This widget will be used to control vertical scroll position.
  - Scrollbar based widget with name suffix "__auto_hscrollbar__". This widget will be used to control horizontal scroll position.

<a id="fal_baseclass_ref_sec_13"></a>
## CEGUI/MenuItem

Base class providing logic for a MenuItem - intended for attaching to Menubar and PopupMenu based widgets.

You should use a "Core/MenuItem" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_14"></a>
## CEGUI/Menubar

Base class providing logic for a menu bar.

You should use a "Core/Menubar" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_15"></a>
## CEGUI/MultiColumnList

Base class providing logic for a multi-column list / grid widget supporting simple items based on non-window class ListboxItem.

You should use a "Core/MultiColumnList" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Scrollbar based widget with name suffix "__auto_vscrollbar__". This widget will be used to control vertical scroll position.
  - Scrollbar based widget with name suffix "__auto_hscrollbar__". This widget will be used to control horizontal scroll position.
  - ListHeader based widget with name suffix "__auto_listheader__". This widget will be used for the header (though technically, you can place it anywhere).

<a id="fal_baseclass_ref_sec_16"></a>
## CEGUI/MultiLineEditbox

Base class providing logic for a more advanced editbox / text box with support for multiple lines of text, word-wrapping, and so on.

You should use a "Core/MultiLineEditbox" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Scrollbar based widget with name suffix "__auto_vscrollbar__". This widget will be used to control vertical scroll position.
  - Scrollbar based widget with name suffix "__auto_hscrollbar__". This widget will be used to control horizontal scroll position.
- Property initialiser definitions:
  - SelectionBrushImage - defines name of image that will be painted for the text selection (this is applied on a per-line basis).

<a id="fal_baseclass_ref_sec_17"></a>
## CEGUI/PopupMenu

Base class providing logic for a pop-up menu.

You should use a "Core/PopupMenu" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_18"></a>
## CEGUI/ProgressBar

Base class providing logic for progress bar widgets.

You should use a "Core/ProgressBar" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_19"></a>
## CEGUI/PushButton

Base class providing logic for a simple push button type widget.

You should use a "Core/Button" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_20"></a>
## CEGUI/RadioButton

Base class providing logic for radio button style widgets.

You should use a "Core/ToggleButton" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_21"></a>
## CEGUI/ScrollablePane

Base class providing logic for a widget that can scroll the content attached to it - which may cover an area much larger than the viewable area.

You should use a "Core/ScrollablePane" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Scrollbar based widget with name suffix "__auto_vscrollbar__". This widget will be used to control vertical scroll position.
  - Scrollbar based widget with name suffix "__auto_hscrollbar__". This widget will be used to control horizontal scroll position.

<a id="fal_baseclass_ref_sec_22"></a>
## CEGUI/Scrollbar

Base class providing logic for a scrollbar type widget with a movable thumb and increase / decrease buttons.

You should use a "Core/Scrollbar" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Thumb based widget with name suffix "__auto_thumb__". This widget will be used for the scrollbar thumb.
  - PushButton based widget with name suffix "__auto_incbtn__". This widget will be used as the increase button.
  - PushButton based widget with name suffix "__auto_decbtn__". This widget will be used as the decrease button.

<a id="fal_baseclass_ref_sec_23"></a>
## CEGUI/Slider

Base class providing logic for a simple slider widget with a movable thumb.

You should use a "Core/Slider" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Thumb based widget with name suffix "__auto_thumb__". This widget will be used for the slider thumb.

<a id="fal_baseclass_ref_sec_24"></a>
## CEGUI/Spinner

Base class providing logic for a numerical spinner widget, with a text entry box and increase / decrease buttons.

You should use a "Core/Default" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Editbox based widget with name suffix "__auto_editbox__". This widget will be used as the text box / display portion of the widget.
  - PushButton based widget with name suffix "__auto_incbtn__". This widget will be used as the increase button.
  - PushButton based widget with name suffix "__auto_decbtn__". This widget will be used as the decrease button.

<a id="fal_baseclass_ref_sec_25"></a>
## CEGUI/TabButton

Base class providing logic for the tabs within a TabControl widget.

You should use a "Core/TabButton" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_26"></a>
## CEGUI/TabControl

Base class providing logic for a widget supporting multiple tabbed content pages.

You should use a "Core/TabControl" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - TabPane based widget with name suffix "__auto_TabPane__". This widget will be used as the content viewing pane.
  - DefaultWindow based widget with name suffix "__auto_TabPane__Buttons". This widget will be used as a container for the tab buttons. Optional.
  - PushButton based widget with name suffix "__auto_TabPane__ScrollLeft". This widget is used to scroll the tab bar buttons left. Optional.
  - PushButton based widget with name suffix "__auto_TabPane__ScrollRight". This widget is used to scroll the tab bar buttons right. Optional.

<a id="fal_baseclass_ref_sec_27"></a>
## CEGUI/Thumb

Base class providing logic for a movable 'tumb' button; for use as a component in other widgets such as scrollbars and sliders.

You should use a "Core/Button" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_28"></a>
## CEGUI/Titlebar

Base class providing logic for a title / caption bar. This should only be used as a component of the FrameWindow widget.

You should use a "Core/Titlebar" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_29"></a>
## CEGUI/Tooltip

Base class providing logic for a simple tooltip type widget.

You should use a "Core/Tooltip" window renderer for this widget.

Assigned WidgetLook should provide the following:

- This class currently has no WidgetLook requirements.

<a id="fal_baseclass_ref_sec_30"></a>
## CEGUI/Tree

Base class providing logic for a basic Tree type widget.

You should use a "Core/Tree" window renderer for this widget.

Assigned WidgetLook should provide the following:

- Child widget definitions:
  - Scrollbar based widget with name suffix "__auto_vscrollbar__". This widget will be used to control vertical scroll position.
  - Scrollbar based widget with name suffix "__auto_hscrollbar__". This widget will be used to control horizontal scroll position.
- Imagery section definitions:
  - ImagerySection named "OpenTreeButton". This imagery is diplayed for the root of a subtree that is closed / collapsed to indicate that the subtree may be opened / expanded.
  - ImagerySection named "CloseTreeButton". This imagery is diplayed for the root of a subtree that is opened / expanded to indicate that the subtree may be closed / collapsed.

---

Copyright (c) 2006 - 2011 Paul D Turner & The CEGUI Development Team

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation; with
no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in [GNU-FDL-1.2.md](GNU-FDL-1.2.md).

*Modified version:* converted from the Doxygen sources of CEGUI 0.8.7 to Markdown.
Only formatting was changed; the text is the original.
