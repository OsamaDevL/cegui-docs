<a id="fal_wr_ref"></a>
# Falagard Window Renderer Requirements

> CEGUI 0.8.7 · Falagard skinning system · converted from [`fal_wr_ref.dox`](https://github.com/cegui/cegui/blob/v0-8-7/doc/doxygen/falagard/fal_wr_ref.dox) ([original page](https://static.cegui.org.uk/docs/0.8.7/fal_wr_ref.html)). Text unchanged; format only.

<a id="fal_wr_ref_sec_0"></a>
## Section Contents

- [Falagard/Button](#fal_wr_ref_sec_1)
- [Falagard/Default](#fal_wr_ref_sec_2)
- [Falagard/Editbox](#fal_wr_ref_sec_3)
- [Falagard/FrameWindow](#fal_wr_ref_sec_4)
- [Falagard/ItemEntry](#fal_wr_ref_sec_5)
- [Falagard/ItemListbox](#fal_wr_ref_sec_6)
- [Falagard/Listbox](#fal_wr_ref_sec_7)
- [Falagard/ListHeader](#fal_wr_ref_sec_8)
- [Falagard/ListHeaderSegment](#fal_wr_ref_sec_9)
- [Falagard/Menubar](#fal_wr_ref_sec_10)
- [Falagard/MenuItem](#fal_wr_ref_sec_11)
- [Falagard/MultiColumnList](#fal_wr_ref_sec_12)
- [Falagard/MultiLineEditbox](#fal_wr_ref_sec_13)
- [Falagard/PopupMenu](#fal_wr_ref_sec_14)
- [Falagard/ProgressBar](#fal_wr_ref_sec_15)
- [Falagard/ToggleButton](#fal_wr_ref_sec_16)
- [Falagard/ScrollablePane](#fal_wr_ref_sec_17)
- [Falagard/Scrollbar](#fal_wr_ref_sec_18)
- [Falagard/Slider](#fal_wr_ref_sec_19)
- [Falagard/Static](#fal_wr_ref_sec_20)
- [Falagard/StaticImage](#fal_wr_ref_sec_21)
- [Falagard/StaticText](#fal_wr_ref_sec_22)
- [Falagard/SystemButton](#fal_wr_ref_sec_23)
- [Falagard/TabButton](#fal_wr_ref_sec_24)
- [Falagard/TabControl](#fal_wr_ref_sec_25)
- [Falagard/Titlebar](#fal_wr_ref_sec_26)
- [Falagard/Tooltip](#fal_wr_ref_sec_27)
- [Falagard/Tree](#fal_wr_ref_sec_28)

<a id="fal_wr_ref_sec_1"></a>
## Falagard/Button

General purpose push button widget class.

Assigned WidgetLook should provide the following:

- StateImagery definitions (missing states will default to 'Normal'):
  - Normal - Imagery used when the widget is neither pushed nor has the mouse hovering over it.
  - Hover - Imagery used when the widget is not pushed and has the mouse hovering over it.
  - Pushed - Imagery used when the widget is pushed and the mouse is over the widget.
  - PushedOff - Imagery used when the widget is pushed and the mouse is not over the widget.
  - Disabled - Imagery used when the widget is disabled.

<a id="fal_wr_ref_sec_2"></a>
## Falagard/Default

Generic window which can be used as a container window, amongst other uses.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.

<a id="fal_wr_ref_sec_3"></a>
## Falagard/Editbox

General purpose single-line text box widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - Imagery used when widget is enabled.
  - Disabled - Imagery used when widget is disabled.
  - ReadOnly - Imagery used when widget is in 'Read Only' state.
  - ActiveSelection - Additional imagery used when a text selection is defined and the widget is active. The imagery for this state will be rendered within the selection area.
  - InactiveSelection - Additional imagery used when a text selection is defined and the widget is not active. The imagery for this state will be rendered within the selection area.
- NamedArea definitions:
  - TextArea - Defines the area where the text, carat, and any selection imagery will appear.
- PropertyDefinition specifications (optional, defaults will be black):
  - NormalTextColour - property that accesses a colour value to be used to render normal unselected text.
  - SelectedTextColour - property that accesses a colour value to be used to render selected text.
- ImagerySection definitions:
  - Carat - Additional imagery used to display the insertion position carat.

<a id="fal_wr_ref_sec_4"></a>
## Falagard/FrameWindow

General purpose window type which can be sized and moved.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - ActiveWithTitleWithFrame - Imagery used when the widget has its title bar enabled, has its frame enabled, and is active.
  - InactiveWithTitleWithFrame - Imagery used when the widget has its title bar enabled, has its frame enabled, and is inactive.
  - DisabledWithTitleWithFrame - Imagery used when the widget has its title bar enabled, has its frame enabled, and is disabled.
  - ActiveWithTitleNoFrame - Imagery used when the widget has its title bar enabled, has its frame disabled, and is active.
  - InactiveWithTitleNoFrame - Imagery used when the widget has its title bar enabled, has its frame disabled, and is inactive.
  - DisabledWithTitleNoFrame - Imagery used when the widget has its title bar enabled, has its frame disabled, and is disabled.
  - ActiveNoTitleWithFrame - Imagery used when the widget has its title bar disabled, has its frame enabled, and is active.
  - InactiveNoTitleWithFrame - Imagery used when the widget has its title bar disabled, has its frame enabled, and is inactive.
  - DisabledNoTitleWithFrame - Imagery used when the widget has its title bar disabled, has its frame enabled, and is disabled.
  - ActiveNoTitleNoFrame - Imagery used when the widget has its title bar disabled, has its frame disabled, and is active.
  - InactiveNoTitleNoFrame - Imagery used when the widget has its title bar disabled, has its frame disabled, and is inactive.
  - DisabledNoTitleNoFrame - Imagery used when the widget has its title bar disabled, has its frame disabled, and is disabled.
- NamedArea definitions:
  - ClientWithTitleWithFrame - Area that defines the clipping region for the client area when the widget has its title bar enabled, and has its frame enabled.
  - ClientWithTitleNoFrame - Area that defines the clipping region for the client area when the widget has its title bar enabled, and has its frame disabled.
  - ClientNoTitleWithFrame - Area that defines the clipping region for the client area when the widget has its title bar disabled, and has its frame enabled.
  - ClientNoTitleNoFrame - Area that defines the clipping region for the client area when the widget has its title bar disabled, and has its frame disabled.

<a id="fal_wr_ref_sec_5"></a>
## Falagard/ItemEntry

Basic class that may be added to any of the ItemListBase base classes.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - ContentSize - Area defining the size of the item content. Required.

<a id="fal_wr_ref_sec_6"></a>
## Falagard/ItemListbox

Improved single column list widget that is able to make use of ItemEntry based windows for listbox items.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions (you should choose one set, or the other):
  - ItemRenderArea - Target area where list items will appear when no scrollbars are visible (also acts as default area). Required.
  - ItemRenderAreaHScroll - Target area where list items will appear when the horizontal scrollbar is visible. Optional.
  - ItemRenderAreaVScroll - Target area where list items will appear when the vertical scrollbar is visible. Optional.
  - ItemRenderAreaHVScroll - Target area where list items will appear when both the horizontal and vertical scrollbars are visible. Optional.
- OR:
  - ItemRenderingArea - Target area where list items will appear when no scrollbars are visible (also acts as default area). Required.
  - ItemRenderingAreaHScroll - Target area where list items will appear when the horizontal scrollbar is visible. Optional.
  - ItemRenderingAreaVScroll - Target area where list items will appear when the vertical scrollbar is visible. Optional.
  - ItemRenderingAreaHVScroll - Target area where list items will appear when both the horizontal and vertical scrollbars are visible. Optional.

<a id="fal_wr_ref_sec_7"></a>
## Falagard/Listbox

General purpose single column list widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions (you should choose one set, or the other):
  - ItemRenderingArea - Target area where list items will appear when no scrollbars are visible (also acts as default area). Required.
  - ItemRenderingAreaHScroll - Target area where list items will appear when the horizontal scrollbar is visible. Optional.
  - ItemRenderingAreaVScroll - Target area where list items will appear when the vertical scrollbar is visible. Optional.
  - ItemRenderingAreaHVScroll - Target area where list items will appear when both the horizontal and vertical scrollbars are visible. Optional.
- OR:
  - ItemRenderArea - Target area where list items will appear when no scrollbars are visible (also acts as default area). Required.
  - ItemRenderAreaHScroll - Target area where list items will appear when the horizontal scrollbar is visible. Optional.
  - ItemRenderAreaVScroll - Target area where list items will appear when the vertical scrollbar is visible. Optional.
  - ItemRenderAreaHVScroll - Target area where list items will appear when both the horizontal and vertical scrollbars are visible. Optional.

<a id="fal_wr_ref_sec_8"></a>
## Falagard/ListHeader

List header widget. Acts as a container for ListHeaderSegment based widgets. Usually used as a component part widget for multi-column list widgets.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- Property initialiser definitions:
  - SegmentWidgetType - specifies the name of a "ListHeaderSegment" based widget type; an instance of which will be created for each column within the header. (Required)

<a id="fal_wr_ref_sec_9"></a>
## Falagard/ListHeaderSegment

Widget type intended for use as a single column header within a list header widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Disabled - Imagery to use when the widget is disabled.
  - Normal - Imagery to use when the widget is enabled and the mouse is not within any part of the segment widget.
  - Hover - Imagery to use when the widget is enabled and the mouse is within the main area of the widget (not the drag-sizing 'splitter' area).
  - SplitterHover - Imagery to use when the widget is enabled and the mouse is within the drag-sizing 'splitter' area.
  - DragGhost - Imagery to use for the drag-moving 'ghost' of the segment. This state should specify that its imagery be render unclipped.
  - AscendingSortIcon - Additional imagery used when the segment has the ascending sort direction set.
  - DescendingSortDown - Additional imagery used when the segment has the descending sort direction set.
  - GhostAscendingSortIcon - Additional imagery used for the drag-moving 'ghost' when the segment has the ascending sort direction set.
  - GhostDescendingSortDown - Additional imagery used for the drag-moving 'ghost' when the segment has the descending sort direction set.
- Property initialiser definitions:
  - MovingCursorImage - Property to define a mouse cursor image to use when drag-moving the widget. (Optional).
  - SizingCursorImage - Property to define a mouse cursor image to use when drag-sizing the widget. (Optional).

<a id="fal_wr_ref_sec_10"></a>
## Falagard/Menubar

General purpose horizontal menu bar widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - ItemRenderArea - Target area where menu items will appear.

<a id="fal_wr_ref_sec_11"></a>
## Falagard/MenuItem

General purpose textual menu item widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - EnabledNormal - Imagery used when the item is enabled and the mouse is not within its area.
  - EnabledHover - Imagery used when the item is enabled and the mouse is within its area.
  - EnabledPushed - Imagery used when the item is enabled and user has pushed the mouse button over it.
  - EnabledPopupOpen - Imagery used when the item is enabled and attached popup menu is opened.
  - DisabledNormal - Imagery used when the item is disabled and the mouse is not within its area.
  - DisabledHover - Imagery used when the item is disabled and the mouse is within its area.
  - DisabledPushed - Imagery used when the item is disabled and user has pushed the mouse button over it.
  - DisabledPopupOpen - Imagery used when the item is disabled and attached popup menu is opened.
  - PopupClosedIcon - Additional imagery used when the item is attached to a popup menu widget and has a a 'sub' popup menu attached to itself, and that popup is closed.
  - PopupOpenIcon - Additional imagery used when the item is attached to a popup menu widget and has a a 'sub' popup menu attached to itself, and that popup is open.
- NamedArea definitions:
  - ContentSize - Area defining the size of this item's content. Required.
  - HasPopupContentSize - Area defining the size of this item's content if the item has an attached popup menu and is not attached to a Menubar (basically the content size with allowance for the 'popup icon'. Optional.

<a id="fal_wr_ref_sec_12"></a>
## Falagard/MultiColumnList

General purpose multi-column list / grid widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - ItemRenderingArea - Target area where list items will appear when no scrollbars are visible (also acts as default area). Required.
  - ItemRenderingAreaHScroll - Target area where list items will appear when the horizontal scrollbar is visible. Optional.
  - ItemRenderingAreaVScroll - Target area where list items will appear when the vertical scrollbar is visible. Optional.
  - ItemRenderingAreaHVScroll - Target area where list items will appear when both the horizontal and vertical scrollbars are visible. Optional.

<a id="fal_wr_ref_sec_13"></a>
## Falagard/MultiLineEditbox

General purpose multi-line text box widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - Imagery used when widget is enabled.
  - Disabled - Imagery used when widget is disabled.
  - ReadOnly - Imagery used when widget is in 'Read Only' state.
- NamedArea definitions:
  - TextArea - Target area where text lines will appear when no scrollbars are visible (also acts as default area). Required.
  - TextAreaHScroll - Target area where text lines will appear when the horizontal scrollbar is visible. Optional.
  - TextAreaVScroll - Target area where text lines will appear when the vertical scrollbar is visible. Optional.
  - TextAreaHVScroll - Target area where text lines will appear when both the horizontal and vertical scrollbars are visible. Optional.
- ImagerySection definitions:
  - Carat - Additional imagery used to display the insertion position carat.
- PropertyDefinition specifications (optional, defaults will be black):
  - NormalTextColour - property that accesses a colour value to be used to render normal unselected text.
  - SelectedTextColour - property that accesses a colour value to be used to render selected text.
  - ActiveSelectionColour - property that accesses a colour value to be used to render active selection highlight.
  - InactiveSelectionColour - property that accesses a colour value to be used to render inactive selection highlight.

<a id="fal_wr_ref_sec_14"></a>
## Falagard/PopupMenu

General purpose popup menu widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - ItemRenderArea - Target area where menu items will appear.

<a id="fal_wr_ref_sec_15"></a>
## Falagard/ProgressBar

General purpose progress widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery used when widget is enabled.
  - Disabled - General imagery used when widget is disabled.
  - EnabledProgress - imagery for 100\ progress used when widget is enabled. The drawn imagery will appear in named area "ProgressArea" and will be clipped appropriately according to widget settings and the current progress value.
  - DisabledProgress - imagery for 100\ progress used when widget is disabled. The drawn imagery will appear in named area "ProgressArea" and will be clipped appropriately according to widget settings and the current progress value.
- NamedArea definitions:
  - ProgressArea - Target area where progress imagery will appear.
- Property initialiser definitions:
  - VerticalProgress - boolean property. Determines whether the progress widget is horizontal or vertical. Default is horizontal. Optional.
  - ReversedProgress - boolean property. Determines whether the progress grows in the opposite direction to what is considered 'usual'. Set to "True" to have progress grow towards the left or bottom of the progress area. Optional.

<a id="fal_wr_ref_sec_16"></a>
## Falagard/ToggleButton

General purpose radio button style widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions (missing states will default to 'Normal' or 'SelectedNormal'):
  - Normal - Imagery used when the widget is in the deselected / off state, and is neither pushed nor has the mouse hovering over it.
  - Hover - Imagery used when the widget is in the deselected / off state, and has the mouse hovering over it.
  - Pushed - Imagery used when the widget is in the deselected / off state, is pushed and has mouse over the widget.
  - PushedOff - Imagery used when the widget is in the deselected / off state, is pushed and does not have the mouse over the widget.
  - Disabled - Imagery used when the widget is in the deselected / off state, and is disabled.
  - SelectedNormal - Imagery used when the widget is in the selected / on state, and is neither pushed nor has the mouse hovering over it.
  - SelectedHover - Imagery used when the widget is in the selected / on state, and has the mouse hovering over it.
  - SelectedPushed - Imagery used when the widget is in the selected / on state, is pushed and has the mouse over the widget.
  - SelectedPushedOff - Imagery used when the widget is in the selected / on state, is pushed and does not have the mouse over the widget.
  - SelectedDisabled - Imagery used when the widget is in the selected / on state, and is disabled.

<a id="fal_wr_ref_sec_17"></a>
## Falagard/ScrollablePane

General purpose scrollable pane widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - ViewableArea - Target area where visible content will appear when no scrollbars are visible (also acts as default area). Required.
  - ViewableAreaHScroll - Target area where visible content will appear when the horizontal scrollbar is visible. Optional.
  - ViewableAreaVScroll - Target area where visible content will appear when the vertical scrollbar is visible. Optional.
  - ViewableAreaHVScroll - Target area where visible content will appear when both the horizontal and vertical scrollbars are visible. Optional.

<a id="fal_wr_ref_sec_18"></a>
## Falagard/Scrollbar

General purpose scrollbar widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - ThumbTrackArea - Target area in which thumb may be moved.
- Property initialiser definitions:
  - VerticalScrollbar - boolean property. Indicates whether this scrollbar will operate in the vertical or horizontal direction. Default is for horizontal. Optional.

<a id="fal_wr_ref_sec_19"></a>
## Falagard/Slider

General purpose slider widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - ThumbTrackArea - Target area in which thumb may be moved.
- Property initialiser definitions:
  - VerticalSlider - boolean property. Indicates whether this slider will operate in the vertical or horizontal direction. Default is for horizontal. Optional.

<a id="fal_wr_ref_sec_20"></a>
## Falagard/Static

Generic non-interactive 'static' widget. Used as a base class for Falagard/StaticImage and Falagard/StaticText.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
  - EnabledFrame - Additional imagery used when the widget is enabled and the widget frame is enabled.
  - DisabledFrame - Additional imagery used when the widget is disabled and the widget frame is enabled.
  - WithFrameEnabledBackground - Additional imagery used when the widget is enabled, the widget frame is enabled, and the widget background is enabled.
  - WithFrameDisabledBackground - Additional imagery used when the widget is disabled, the widget frame is enabled, and the widget background is enabled.
  - NoFrameEnabledBackground - Additional imagery used when the widget is enabled, the widget frame is disabled, and the widget background is enabled.
  - NoFrameDisabledBackground - Additional imagery used when the widget is disabled, the widget frame is disabled, and the widget background is enabled.

<a id="fal_wr_ref_sec_21"></a>
## Falagard/StaticImage

Static widget that displays a configurable image.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
  - EnabledFrame - Additional imagery used when the widget is enabled and the widget frame is enabled.
  - DisabledFrame - Additional imagery used when the widget is disabled and the widget frame is enabled.
  - WithFrameEnabledBackground - Additional imagery used when the widget is enabled, the widget frame is enabled, and the widget background is enabled.
  - WithFrameDisabledBackground - Additional imagery used when the widget is disabled, the widget frame is enabled, and the widget background is enabled.
  - NoFrameEnabledBackground - Additional imagery used when the widget is enabled, the widget frame is disabled, and the widget background is enabled.
  - NoFrameDisabledBackground - Additional imagery used when the widget is disabled, the widget frame is disabled, and the widget background is enabled.
  - WithFrameImage - Image rendering when the frame is enabled.
  - NoFrameImage - Image rendering when the frame is disabled.

<a id="fal_wr_ref_sec_22"></a>
## Falagard/StaticText

Static widget that displays configurable text.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
  - EnabledFrame - Additional imagery used when the widget is enabled and the widget frame is enabled.
  - DisabledFrame - Additional imagery used when the widget is disabled and the widget frame is enabled.
  - WithFrameEnabledBackground - Additional imagery used when the widget is enabled, the widget frame is enabled, and the widget background is enabled.
  - WithFrameDisabledBackground - Additional imagery used when the widget is disabled, the widget frame is enabled, and the widget background is enabled.
  - NoFrameEnabledBackground - Additional imagery used when the widget is enabled, the widget frame is disabled, and the widget background is enabled.
  - NoFrameDisabledBackground - Additional imagery used when the widgetis disabled, the widget frame is disabled, and the widget background is enabled.
- NamedArea definitions (missing areas will default to WithFrameTextRenderArea):
  - WithFrameTextRenderArea - Target area where text will appear when the frame is enabled and no scrollbars are visible (also acts as default area). Required.
  - WithFrameTextRenderAreaHScroll - Target area where text will appear when the frame is enabled and the horizontal scrollbar is visible. Optional.
  - WithFrameTextRenderAreaVScroll - Target area where text will appear when the frame is enabled and the vertical scrollbar is visible. Optional.
  - WithFrameTextRenderAreaHVScroll - Target area where text will appear when the frame is enabled and both the horizontal and vertical scrollbars are visible. Optional.
  - NoFrameTextRenderArea - Target area where text will appear when the frame is disabled and no scrollbars are visible (also acts as default area). Optional.
  - NoFrameTextRenderAreaHScroll - Target area where text will appear when the frame is disabled and the horizontal scrollbar is visible. Optional.
  - NoFrameTextRenderAreaVScroll - Target area where text will appear when the frame is disabled and the vertical scrollbar is visible. Optional.
  - NoFrameTextRenderAreaHVScroll - Target area where text will appear when the frame is disabled and both the horizontal and vertical scrollbars are visible. Optional.
- Child widget definitions:
  - Scrollbar based widget with name suffix "__auto_vscrollbar__". This widget will be used to control vertical scroll position.
  - Scrollbar based widget with name suffix "__auto_hscrollbar__". This widget will be used to control horizontal scroll position.

<a id="fal_wr_ref_sec_23"></a>
## Falagard/SystemButton

Specialised push button widget intended to be used for 'system' buttons appearing outside of the client area of a frame window style widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions (missing states will default to 'Normal'):
  - Normal - Imagery used when the widget is neither pushed nor has the mouse hovering over it.
  - Hover - Imagery used when the widget is not pushed and has the mouse hovering over it.
  - Pushed - Imagery used when the widget is pushed and the mouse is over the widget.
  - PushedOff - Imagery used when the widget is pushed and the mouse is not over the widget.
  - Disabled - Imagery used when the widget is disabled.

<a id="fal_wr_ref_sec_24"></a>
## Falagard/TabButton

Special widget type used for tab buttons within a tab control based widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions (missing states will default to 'Normal'):
  - Normal - Imagery used when the widget is neither selected nor has the mouse hovering over it.
  - Hover - Imagery used when the widget has the mouse hovering over it.
  - Selected - Imagery used when the widget is the active / selected tab.
  - Disabled - Imagery used when the widget is disabled.

<a id="fal_wr_ref_sec_25"></a>
## Falagard/TabControl

General purpose tab control widget.

The current TabControl base class enforces a fairly strict layout, so while imagery can be customised as desired, the general layout of the component widgets is, at least for the time being, mostly fixed.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- Property initialiser definitions:
  - TabButtonType - specifies a TabButton based widget type to be created each time a new tab button is required.

<a id="fal_wr_ref_sec_26"></a>
## Falagard/Titlebar

Title bar widget intended for use as the title bar of a frame window widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions (missing states will default to 'Normal'):
  - Active - Imagery used when the widget is active.
  - Inactive - Imagery used when the widget is inactive.
  - Disabled - Imagery used when the widget is disabled.

<a id="fal_wr_ref_sec_27"></a>
## Falagard/Tooltip

General purpose tool-tip widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - TextArea - Typically this would be the same area as the TextComponent you define to receive the tool-tip text. This named area is used when deciding how to dynamically size the tool-tip so that text is not clipped.

<a id="fal_wr_ref_sec_28"></a>
## Falagard/Tree

Basic Tree type widget.

Assigned WidgetLook should provide the following:

- StateImagery definitions:
  - Enabled - General imagery for when the widget is enabled.
  - Disabled - General imagery for when the widget is disabled.
- NamedArea definitions:
  - ItemRenderingArea - Target area where tree items will appear when no scrollbars are visible (also acts as default area). Required.
  - ItemRenderingAreaHScroll - Target area where tree items will appear when the horizontal scrollbar is visible. Optional.
  - ItemRenderingAreaVScroll - Target area where tree items will appear when the vertical scrollbar is visible. Optional.
  - ItemRenderingAreaHVScroll - Target area where tree items will appear when both the horizontal and vertical scrollbars are visible. Optional.

---

Copyright (c) 2006 - 2011 Paul D Turner & The CEGUI Development Team

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation; with
no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in [GNU-FDL-1.2.md](GNU-FDL-1.2.md).

*Modified version:* converted from the Doxygen sources of CEGUI 0.8.7 to Markdown.
Only formatting was changed; the text is the original.
