<a id="fal_enum_ref"></a>
# Falagard XML Enumeration Reference

> CEGUI 0.8.7 · Falagard skinning system · converted from [`fal_enum_ref.dox`](https://github.com/cegui/cegui/blob/v0-8-7/doc/doxygen/falagard/fal_enum_ref.dox) ([original page](https://static.cegui.org.uk/docs/0.8.7/fal_enum_ref.html)). Text unchanged; format only.

<a id="fal_enum_ref_sec_0"></a>
## Section Contents

- [DimensionOperator Enumeration](#fal_enum_ref_sec_1)
- [DimensionType Enumeration](#fal_enum_ref_sec_2)
- [FontMetricType Enumeration](#fal_enum_ref_sec_3)
- [FrameImageComponent Enumeration](#fal_enum_ref_sec_4)
- [HorizontalAlignment Enumeration](#fal_enum_ref_sec_5)
- [HorizontalFormat Enumeration](#fal_enum_ref_sec_6)
- [HorizontalTextFormat Enumeration](#fal_enum_ref_sec_7)
- [PropertyType Enumeration](#fal_enum_ref_sec_8)
- [VerticalAlignment Enumeration](#fal_enum_ref_sec_9)
- [VerticalFormat Enumeration](#fal_enum_ref_sec_10)
- [VerticalTextFormat Enumeration](#fal_enum_ref_sec_11)
- [ChildEventAction Enumeration](#fal_enum_ref_sec_12)

<a id="fal_enum_ref_sec_1"></a>
## DimensionOperator Enumeration

- `"Noop"`  does nothing.
- `"Add"`  Adds two dimensions.
- `"Subtract"`  Subtracts two dimensions.
- `"Multiply"`  Multiplies two dimensions.
- `"Divide"`  Divides two dimensions.

<a id="fal_enum_ref_sec_2"></a>
## DimensionType Enumeration

- `"LeftEdge"`  specifies the left edge of the target item.
- `"TopEdge"`  specifies the top edge of the target item.
- `"RightEdge"`  specifies the right edge of the target item.
- `"BottomEdge"`  specifies the bottom edge of the target item.
- `"XPosition"`  specifies the x position co-ordinate of the target item (same as ?LeftEdge?).
- `"YPosition"`  specifies the y position co-ordinate of the target item (same as ?TopEdge?).
- `"Width"`  specifies the width of the target item.
- `"Height"`  specifies the height of the target item.
- `"XOffset"`  specifies the x offset of the target item (only applies to Images).
- `"YOffset"`  specifies the y offset of the target item (only applies to Images).

<a id="fal_enum_ref_sec_3"></a>
## FontMetricType Enumeration

- `"LineSpacing"`  gets the vertical line spacing value of the font.
- `"Baseline"`  get the vertical baseline value of the font.
- `"HorzExtent"`  gets the horizontal extent of a string of text.

<a id="fal_enum_ref_sec_4"></a>
## FrameImageComponent Enumeration

- `"TopLeftCorner"`  specifies the image be used for the frame's top-left corner.
- `"TopRightCorner"`  specifies the image be used for the frame's top-right corner.
- `"BottomLeftCorner"`  specifies the image be used for the frame's bottom-left corner.
- `"BottomRightCorner"`  specifies the image be used for the frame's bottom-right corner.
- `"LeftEdge"`  specifies the image be used for the frame' left edge.
- `"RightEdge"`  specifies the image be used for the frame's right edge.
- `"TopEdge"`  specifies the image be used for the frame's top edge.
- `"BottomEdge"`  specifies the image be used for the frame bottom edge.
- `"Background"`  specifies the image be used for the frame's background (area formed within all edges).

<a id="fal_enum_ref_sec_5"></a>
## HorizontalAlignment Enumeration

- `"LeftAligned"`  x position is an offset of element's left edges.
- `"CentreAligned"`  x position is an offset of element's horizontal centre points.
- `"RightAligned"`  x position is an offset of element's right edges.

<a id="fal_enum_ref_sec_6"></a>
## HorizontalFormat Enumeration

- `"LeftAligned"`  Image is left aligned within the prescribed area.
- `"CentreAligned"`  Image is horizontally centred within the prescribed area.
- `"RightAligned"`  Image is right aligned within the prescribed area.
- `"Stretched"`  Image is horizontally stretched to fill the prescribed area.
- `"Tiled"`  Image is horizontally tiled to fill the prescribed area.

<a id="fal_enum_ref_sec_7"></a>
## HorizontalTextFormat Enumeration

- `"LeftAligned"`  lines of text are left aligned within the prescribed area.
- `"CentreAligned"`  lines of text are horizontally centred within the prescribed area.
- `"RightAligned"`  lines of text are right aligned within the prescribed area.
- `"Justified"`  lines of text are justified to the prescribed area.
- `"WordWrapLeftAligned"`  text wraps, with lines left aligned within the prescribed area.
- `"WordWrapCentreAligned"`  text wraps, with lines horizontally centred in the prescribed area.
- `"WordWrapRightAligned"`  text wraps, with lines right aligned within the prescribed area.
- `"WordWrapJustified"`  text wraps, within lines justified to the prescribed area.

<a id="fal_enum_ref_sec_8"></a>
## PropertyType Enumeration

- `"Generic"`  specifies a general purpose property (accessed as CEGUI::String).
- `"Colour"`  specifies a property that accesses a single CEGUI::Colour value.
- `"ColourRect"`  specifies a property that accesses a CEGUI::ColourRect value.
- `"UBox"`  specifies a property that accesses a CEGUI::UBox value.
- `"URect"`  specifies a property that accesses a CEGUI::URect value.
- `"USize"`  specifies a property that accesses a CEGUI::USize value.
- `"UDim"`  specifies a property that accesses a CEGUI::UDim value.
- `"UVector2"`  specifies a property that accesses a CEGUI::UVector2 value.
- `"Sizef"`  specifies a property that accesses a CEGUI::Sizef value.
- `"Vector2f"`  specifies a property that accesses a CEGUI::Vector2f value.
- `"Vector3f"`  specifies a property that accesses a CEGUI::Vector3f value.
- `"Rectf"`  specifies a property that accesses a CEGUI::Rectf value.
- `"Font"`  specifies a property that accesses a font via its name string.
- `"Image"`  specifies a property that accesses an image via its name string.
- `"Quaternion"`  specifies a property that accesses a CEGUI::Quaternion value.
- `"AspectMode"`  specifies a property that accesses a CEGUI::AspectMode value.
- `"HorizontalAlignment"`  specifies a property that accesses a CEGUI::HorizontalAlignment enumerated value.
- `"VerticalAlignment"`  specifies a property that accesses a CEGUI::VerticalAlignment enumerated value.
- `"HorizontalTextFormatting"`  specifies a property that accesses a CEGUI::HorizontalTextFormatting enumerated value.
- `"VerticalTextFormatting"`  specifies a property that accesses a CEGUI::VerticalTextFormatting enumerated value.
- `"WindowUpdateMode"`  specifies a property that accesses a CEGUI::WindowUpdateMode enumerated value.
- `"bool"`  specifies a property that accesses a simple boolean value.
- `"uint"`  specifies a property that accesses a simple unsigned integer value.
- `"unsigned` long"  specifies a property that accesses a simple unsigned long value.
- `"int"`  specifies a property that accesses a simple signed integer value.
- `"float"`  specifies a property that accesses a simple single precision floating point value.
- `"double"`  specifies a property that accesses a simple double precision floating point value.
- `"TabControl::TabPanePosition"`  specifies a property that accesses a CEGUI::TabControl::TabPanePosition enumerated value.
- `"Spinner::TextInputMode"`  specifies a property that accesses a CEGUI::Spinner::TextInputMode enumerated value.
- `"ItemListBase::SortMode"`  specifies a property that accesses a CEGUI::ItemListBase::SortDirection enumerated value.
- `"ListHeaderSegment::SortDirection"`  specifies a property that accesses a CEGUI::ListHeaderSegment::SortDirection enumerated value.
- `"MultiColumnList::SelectionMode"`  specifies a property that accesses a CEGUI::MultiColumnList::SelectionMode enumerated value.
- `"String"`  specifies a property that accesses a CEGUI::String value.
- `"VertFormatting"`  specifies a property that accesses a CEGUI::VertFormatting enumerated value.
- `"HorzFormatting"`  specifies a property that accesses a CEGUI::HorzFormatting enumerated value.

<a id="fal_enum_ref_sec_9"></a>
## VerticalAlignment Enumeration

- `"TopAligned"`  y position is an offset of element's top edges.
- `"CentreAligned"`  y position is an offset of element's vertical centre points.
- `"BottomAligned"`  y position is an offset of element's bottom edges.

<a id="fal_enum_ref_sec_10"></a>
## VerticalFormat Enumeration

- `"TopAligned"`  Image is aligned with the top of the prescribed area.
- `"CentreAligned"`  Image is vertically centred within the prescribed area.
- `"BottomAligned"`  Image is aligned with the bottom of the prescribed area.
- `"Stretched"`  Image is vertically stretched to fill the prescribed area.
- `"Tiled"`  Image is vertically tiled to fill the prescribed area.

<a id="fal_enum_ref_sec_11"></a>
## VerticalTextFormat Enumeration

- `"TopAligned"`  Text line block is aligned with the top of the prescribed area.
- `"CentreAligned"`  Text line block is vertically centred within the prescribed area.
- `"BottomAligned"`  Text line block is aligned with the bottom of the prescribed area.

<a id="fal_enum_ref_sec_12"></a>
## ChildEventAction Enumeration

- `"Redraw"`  When the event is fired on the child widget, the containing widget will be redrawn (non-recursive).
- `"Layout"`  When the event is fired on the child widget, the containing widget will re-layout its child widget content.

---

Copyright (c) 2006 - 2011 Paul D Turner & The CEGUI Development Team

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation; with
no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in [GNU-FDL-1.2.md](GNU-FDL-1.2.md).

*Modified version:* converted from the Doxygen sources of CEGUI 0.8.7 to Markdown.
Only formatting was changed; the text is the original.
