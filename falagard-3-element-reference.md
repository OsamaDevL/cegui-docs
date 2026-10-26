<a id="fal_element_ref"></a>
# Falagard XML Element Reference

> CEGUI 0.8.7 · Falagard skinning system · converted from [`fal_element_ref.dox`](https://github.com/cegui/cegui/blob/v0-8-7/doc/doxygen/falagard/fal_element_ref.dox) ([original page](https://static.cegui.org.uk/docs/0.8.7/fal_element_ref.html)). Text unchanged; format only.

The following pages contain reference material for the XML elements defined for the Falagard skin definition files.

<a id="fal_elem_ref_sec_0"></a>
## Section Contents

- [Overview](#fal_elem_ref_sec_1)
- [\<AbsoluteDim\> Element](#fal_elem_ref_sec_2)
- [\<Area\> Element](#fal_elem_ref_sec_3)
- [\<AreaProperty\> Element](#fal_elem_ref_sec_4)
- [\<Child\> Element](#fal_elem_ref_sec_5)
- [\<ColourProperty\> Element](#fal_elem_ref_sec_6)
- [\<ColourRectProperty\> Element](#fal_elem_ref_sec_7)
- [\<Colours\> Element](#fal_elem_ref_sec_8)
- [\<Dim\> Element](#fal_elem_ref_sec_9)
- [\<EventAction\> Element](#fal_elem_ref_eventaction)
- [\<EventLinkDefinition\> Element](#fal_elem_ref_eventlinkdefintion)
- [\<EventLinkTarget\> Element](#fal_elem_ref_eventlinktarget)
- [\<Falagard\> Element](#fal_elem_ref_sec_11)
- [\<FontDim\> Element](#fal_elem_ref_sec_12)
- [\<FontProperty\> Element](#fal_elem_ref_sec_13)
- [\<FrameComponent\> Element](#fal_elem_ref_sec_14)
- [\<HorzAlignment\> Element](#fal_elem_ref_sec_15)
- [\<HorzFormat\> Element](#fal_elem_ref_sec_16)
- [\<HorzFormatProperty\> Element](#fal_elem_ref_sec_17)
- [\<Image\> Element](#fal_elem_ref_sec_18)
- [\<ImageDim\> Element](#fal_elem_ref_sec_19)
- [\<ImagePropertyDim\> Element](#fal_elem_ref_sec_imagepropertydim)
- [\<ImageryComponent\> Element](#fal_elem_ref_sec_20)
- [\<ImageProperty\> Element](#fal_elem_ref_sec_21)
- [\<ImagerySection\> Element](#fal_elem_ref_sec_22)
- [\<Layer\> Element](#fal_elem_ref_sec_23)
- [\<NamedArea\> Element](#fal_elem_ref_sec_24)
- [\<OperatorDim\> Element](#fal_elem_ref_sec_operatordim)
- [\<Property\> Element](#fal_elem_ref_sec_25)
- [\<PropertyDefinition\> Element](#fal_elem_ref_sec_26)
- [\<PropertyLinkDefinition\> Element](#fal_elem_ref_sec_27)
- [\<PropertyLinkTarget\> Element](#fal_elem_propertylinktarget)
- [\<PropertyDim\> Element](#fal_elem_ref_sec_28)
- [\<Section\> Element](#fal_elem_ref_sec_29)
- [\<StateImagery\> Element](#fal_elem_ref_sec_30)
- [\<Text\> Element](#fal_elem_ref_sec_31)
- [\<TextComponent\> Element](#fal_elem_ref_sec_32)
- [\<TextProperty\> Element](#fal_elem_ref_sec_33)
- [\<UnifiedDim\> Element](#fal_elem_ref_sec_34)
- [\<VertAlignment\> Element](#fal_elem_ref_sec_35)
- [\<VertFormat\> Element](#fal_elem_ref_sec_36)
- [\<VertFormatProperty\> Element](#fal_elem_ref_sec_37)
- [\<WidgetDim\> Element](#fal_elem_ref_sec_38)
- [\<WidgetLook\> Element](#fal_elem_ref_sec_39)

<a id="fal_elem_ref_sec_1"></a>
## Overview

The reference for each element is arranged into sections, as described below:

<a id="fal_elem_ref_sec_1_1"></a>
### Purpose:

This section describes what the elements general purpose is within the specifications.

<a id="fal_elem_ref_sec_1_2"></a>
### Attributes:

This section describes available attributes for the elements, and whether they are required or optional.

<a id="fal_elem_ref_sec_1_3"></a>
### Usage:

Describes where the element may appear, whether the element may have sub-elements, and other important usage information.

<a id="fal_elem_ref_sec_1_4"></a>
### Examples:

For many elements, this section will contain brief examples showing the element used in context.

<a id="fal_elem_ref_sec_2"></a>
## \<AbsoluteDim\> Element

<a id="fal_elem_ref_sec_2_1"></a>
### Purpose:

The `<AbsoluteDim>` element is used to define a component dimension for an area rectangle. `<AbsoluteDim>` is used to specify absolute pixel values for a dimension.

<a id="fal_elem_ref_sec_2_2"></a>
### Attributes:

- `value`  specifies the a number of pixels. Required attribute.

<a id="fal_elem_ref_sec_2_3"></a>
### Usage:

- The `<AbsoluteDim>` element can appear as a sub-element in `<Dim>` to form a dimension specification for an area.
- The `<AbsoluteDim>` element can appear as a sub-element of `<OperatorDim>` to specify an operand for a dimension calculation.

<a id="fal_elem_ref_sec_2_4"></a>
### Examples:

The following shows `<AbsoluteDim>` used to define an area rectangle. In the example, all four component dimensions of the area rectangle are specified using `<AbsoluteDim>:`

```xml
<Area>
  <Dim type="LeftEdge" >
    <AbsoluteDim value="10" />
  </Dim>
  <Dim type="TopEdge" >
    <AbsoluteDim value="50" />
  </Dim>
  <Dim type="Width" >
    <AbsoluteDim value="290" />
  </Dim>
  <Dim type="Height" >
    <AbsoluteDim value="250" />
  </Dim>
</Area>
```

The following shows `<AbsoluteDim>` in use as part of a dimension calculation sequence. In the example the left edge is being set to the width of the child widget 'myWidget' minus two pixels:

```xml
<Area>
  <Dim type="LeftEdge" >
    <OperatorDim op="Subtract" >
      <WidgetDim widget="myWidget" dimension="Width" />
      <AbsoluteDim value="2" />
    </OperatorDim>
  </Dim>
  ...
</Area>
```

Finally, we see `<AbsoluteDim>` as part of a dimension calculation sequence. In the example, we are adding the value of some window property to the starting absolute value of six:

```xml
<Area>
  ...
  <Dim type="Height" >
    <OperatorDim op="Add" >
      <AbsoluteDim value="6" />
      <PropertyDim name="someHeightProperty" />
    </OperatorDim>
  </Dim>
</Area>
```

<a id="fal_elem_ref_sec_3"></a>
## \<Area\> Element

<a id="fal_elem_ref_sec_3_1"></a>
### Purpose:

The `<Area>` element is a simple container element for the `<Dim>` dimension elements, or a single `<AreaProperty>` element, in order to form a rectangular area. `<Area>` is generally used to define target regions which are to be used for rendering imagery, text, to place a component child widget, or to form 'named' areas required by the base widget.

<a id="fal_elem_ref_sec_3_2"></a>
### Attributes:

`<Area>` has no attributes.

<a id="fal_elem_ref_sec_3_3"></a>
### Usage:

- The `<Area>` element must contain either:
  - A single `<AreaProperty>` element that describes a URect type property where the final area can be obtained.
  - Four `<Dim>` elements:
    - One `<Dim>` element must define the left edge or x position.
    - One `<Dim>` element must define the top edge or y position.
    - One `<Dim>` element must define either the right edge or width.
    - One `<Dim>` element must define either the bottom edge or height.
- The `<Area>` element may appear in any of the following elements:
  - `<Child>` to define the target area to be occupied by a child widget.
  - `<ImageryComponent>` to define the target rendering area of an image.
  - `<NamedArea>` to define an area which can be retrieved by name.
  - `<TextComponent>` to define the target rendering area of some text.
  - `<FrameComponent>` to define the target rendering area for a frame.

<a id="fal_elem_ref_sec_3_4"></a>
### Examples:

In this example we can see a named area being defined:

```xml
<NamedArea name="exampleArea" >
  <Area>
    <Dim type="LeftEdge"><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge"><AbsoluteDim value="0" /></Dim>
    <Dim type="Width"><UnifiedDim scale="1.0" /></Dim>
    <Dim type="Height"><UnifiedDim scale="1.0" /></Dim>
  </Area>
</NamedArea>
```

<a id="fal_elem_ref_sec_4"></a>
## \<AreaProperty\> Element

<a id="fal_elem_ref_sec_4_1"></a>
### Purpose:

The `<AreaProperty>` element is intended to allow the system to access a property on the target window to obtain the final target area of a component being defined.

<a id="fal_elem_ref_sec_4_2"></a>
### Attributes:

- `name`  specifies the name of the property to access. The named property must access a URect value. Required attribute.

<a id="fal_elem_ref_sec_4_3"></a>
### Usage:

- The `<AreaProperty>` element may not contain sub-elements.
- The `<AreaProperty>` element may appear as a sub-element only within the main `<Area>` element.

<a id="fal_elem_ref_sec_4_4"></a>
### Examples:

<a id="fal_elem_ref_sec_5"></a>
## \<Child\> Element

<a id="fal_elem_ref_sec_5_1"></a>
### Purpose:

The `<Child>` element defines a component widget that will be created and added to each instance of any window using the `<WidgetLook>` being defined. Some base widgets have requirements for `<Child>` element definition that must be provided.

<a id="fal_elem_ref_sec_5_2"></a>
### Attributes:

- `type`  specifies the widget type to create. Required attribute.
- `nameSuffix`  specifies a suffix which will be used when naming the widget. The final name of the child widget will be that of the parent with this suffix appended. Required attribute.
- `look`  specifies the name of a widget look to apply to the child widget. You should only use this if 'type' specifies a Falagard base widget type. Optional attribute.
- `autoWindow` specifies whether this child window is to be flagged as an auto-window. Optional attribute, default value is `true.`

<a id="fal_elem_ref_sec_5_3"></a>
### Usage:

Note: the sub-elements should appear in the order that they are defined here.

- The `<Child>` element may contain any number of `<EventAction>` elements that define actions to be taken by the containing widget in response to events being fired on the child widget being defined.
- The `<Child>` element must contain an `<Area>` element that defines the location of the child widget in relation to the component being defined.
- You may optionally specify a single `<VertAlignment>` element to set the vertical alignment for the child.
- You may optionally specify a single `<HorzAlignment>` element to set the horizontal alignment for the child.
- You may specify any number of `<Property>` elements to set default values for any property supported by the widget type being used for the child.
- The `<Child>` element may only appear within the `<WidgetLook>` element.

<a id="fal_elem_ref_sec_5_4"></a>
### Examples:

In this example, taken from TaharezLook.looknfeel, we see how the title bar child widget required by the frame window type is defined:

```xml
<WidgetLook name="TaharezLook/FrameWindow">
  ...
  <Child type="TaharezLook/Titlebar" nameSuffix="__auto_titlebar__">
    <Area>
      <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
      <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
      <Dim type="Width" ><UnifiedDim scale="1" type="Width" /></Dim>
      <Dim type="Height" >
        <OperatorDim op="Multiply">
          <FontDim type="LineSpacing" />
          <AbsoluteDim value="1.5" />
        </OperatorDim>
      </Dim>
    </Area>
    <Property name="AlwaysOnTop" value="False" />
  </Child>
  ...
</WidgetLook>
```

<a id="fal_elem_ref_sec_6"></a>
## \<ColourProperty\> Element

<a id="fal_elem_ref_sec_6_1"></a>
### Purpose:

The `<ColourProperty>` element is intended to allow the system to access a property on the target window to obtain colour information to be used when drawing some part of the component being defined.

<a id="fal_elem_ref_sec_6_2"></a>
### Attributes:

- `name`  specifies the name of the property to access. The named property must access a single colour value. Required attribute.

<a id="fal_elem_ref_sec_6_3"></a>
### Usage:

- The `<ColourProperty>` element may not contain sub-elements.
- The `<ColourProperty>` element may appear as a sub-element within any of the following elements:
  - `<ImageryComponent>` to specify a modulating colour to be applied when rendering the image.
  - `<ImagerySection>` to specify a modulating colour to be applied to all imagery components within the imagery section as it is rendered.
  - `<Section>` to specify a modulating colour to be applied to all imagery in the named section as it is rendered.
  - `<TextComponent>` to specify a colour to use when rendering the text component.
  - `<FrameComponent>` to specify a colour to use when rendering the text frame.

<a id="fal_elem_ref_sec_6_4"></a>
### Examples:

The following example, listing imagery for a button in the "Normal" state, shows the `<ColourProperty>` element in use to specify a property where colours to be used when rendering the ImagerySection named 'label' can be found:

```xml
<StateImagery name="Normal">
  <Layer>
    <Section section="normal" />
    <Section section="label">
      <ColourProperty name="NormalTextColour" />
    </Section>
  </Layer>
</StateImagery>
```

<a id="fal_elem_ref_sec_7"></a>
## \<ColourRectProperty\> Element

<a id="fal_elem_ref_sec_7_1"></a>
### Purpose:

The `<ColourRectProperty` \> element is intended to allow the system to access a property on the target window to obtain colour information to be used when drawing some part of the component being defined.

<a id="fal_elem_ref_sec_7_2"></a>
### Attributes:

- `name`  specifies the name of the property to access. The named property must access a ColourRect value. Required attribute.

<a id="fal_elem_ref_sec_7_3"></a>
### Usage:

- The `<ColourRectProperty>` element may not contain sub-elements.
- The `<ColourRectProperty>` element may appear as a sub-element within any of the following elements:
  - `<ImageryComponent>` to specify a modulating ColourRect to be applied when rendering the image.
  - `<ImagerySection>` to specify a modulating ColourRect to be applied to all imagery components within the imagery section as it is rendered.
  - `<Section>` to specify a modulating ColourRect to be applied to all imagery in the named section as it is rendered.
  - `<TextComponent>` to specify a ColourRect to use when rendering the text component.
  - `<FrameComponent>` to specify a colour to use when rendering the text frame.

<a id="fal_elem_ref_sec_7_4"></a>
### Examples:

```xml
...
<StateImagery name="SpecialState">
  <Layer>
    <Section section="special_main">
      <ColourRectProperty name="SpecialColours" />
    </Section>
  </Layer>
</StateImagery>
...
```

<a id="fal_elem_ref_sec_8"></a>
## \<Colours\> Element

<a id="fal_elem_ref_sec_8_1"></a>
### Purpose:

The `<Colours>` element is used to explicitly specify values for a ColourRect that should be used when rendering some part of the component being defined.

<a id="fal_elem_ref_sec_8_2"></a>
### Attributes:

- `topLeft`  specifies a hex colour value, of the form "AARRGGBB", to be used for the top-left corner of the ColourRect. Required attribute.
- `topRight`  specifies a hex colour value, of the form "AARRGGBB", to be used for the top-right corner of the ColourRect. Required attribute.
- `bottomLeft`  specifies a hex colour value, of the form "AARRGGBB", to be used for the bottom-left corner of the ColourRect. Required attribute.
- `bottomRight`  specifies a hex colour value of the form "AARRGGBB", to be used for the bottom-right corner of the ColourRect. Required attribute.

<a id="fal_elem_ref_sec_8_3"></a>
### Usage:

- The `<Colours>` element may not contain sub-elements.
- The `<Colours>` element may appear as a sub-element within any of the following elements:
  - `<ImageryComponent>` to specify a modulating ColourRect to be applied when rendering the image.
  - `<ImagerySection>` to specify a modulating ColourRect to be applied to all imagery components within the imagery section as it is rendered.
  - `<Section>` to specify a modulating ColourRect to be applied to all imagery in the named section as it is rendered.
  - `<TextComponent>` to specify a ColourRect to use when rendering the text component.
  - `<FrameComponent>` to specify a colour to use when rendering the text frame.

<a id="fal_elem_ref_sec_8_4"></a>
### Examples:

In this example, we see the `<Colours>` element used to specify the value 'FFFFFF00' as the colour for all four corners of the colour rect to be used when rendering the image being defined:

```xml
...
<ImageryComponent>
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="Width" ><AbsoluteDim value="12" /></Dim>
    <Dim type="Height" ><AbsoluteDim value="24" /></Dim>
  </Area>
  <Image imageset="newImageset" image="FunkyComponent" />
  <Colours
    topLeft="FFFFFF00"
    topRight="FFFFFF00"
    bottomLeft="FFFFFF00"
    bottomRight="FFFFFF00"
  />
  <VertFormat type="Stretched" />
  <HorzFormat type="Stretched" />
</ImageryComponent>
...
```

<a id="fal_elem_ref_sec_9"></a>
## \<Dim\> Element

<a id="fal_elem_ref_sec_9_1"></a>
### Purpose:

The `<Dim>` element is intended as a container element for a single dimension of an area rectangle.

<a id="fal_elem_ref_sec_9_2"></a>
### Attributes:

- `type`  specifies what the dimension being defined represents. This attribute should be set to one of the values defined for the DimensionType enumeration (see below). Required attribute.

<a id="fal_elem_ref_sec_9_3"></a>
### Usage:

- The `<Dim>` element may only appear within the `<Area>` element.
- The `<Dim>` element may contain any of the following specialised dimension elements:
  - `<AbsoluteDim>`
  - `<FontDim>`
  - `<ImageDim>`
  - `<ImagePropertyDim>`
  - `<PropertyDim>`
  - `<UnifiedDim>`
  - `<WidgetDim>`
  - `<OperatorDim>`

<a id="fal_elem_ref_sec_9_4"></a>
### Examples:

<a id="fal_elem_ref_eventaction"></a>
## \<EventAction\> Element

<a id="fal_elem_ref_eventaction_1"></a>
### Purpose:

The `<EventAction>` element is used to specify a predefined action that should be performed by the containing widget for the child widget being defined, in response to a specified event being fired by the child widget.

This is useful in situations where the containing widget has imagery or other content that is tied to some state on the child wiget.  By using the facilities provided by \<EventAction\> the containing widget is updated on demand in response to changes on the child.

<a id="fal_elem_ref_eventaction_2"></a>
### Attributes:

- `event` specifies the name of the event on the Child component being defined that will trigger the action.  Required attribute.
- `action` specifies one of the values defined for the [ChildEventAction](falagard-4-enumeration-reference.md#fal_enum_ref_sec_12) enumeration. Required attribute.

<a id="fal_elem_ref_eventaction_3"></a>
### Usage:

- The `<EventAction>` element may not conatin any sub-elements.
- The `<EventAction>` element may only appear as a sub-element within `<Child>` elements.

<a id="fal_elem_ref_eventaction_4"></a>
### Examples:

In this example, an EventAction is defined for the thumb of a slider widget. The definition indicates that when the `Moved` is fired for the thumb widget, the containing slider should redraw itself.  This is useful in scenarios where the slider has imagery whose position is dependent upon the position of the thumb - by using the \<EventAction\> system, the required updates are fully automated.

```xml
<Falagard>
  <WidgetLook name="ANewLook/Slider">
  ...
    <Child  type="ANewLook/SliderThumb" nameSuffix="__auto_thumb__">
      <EventAction event="Moved" action="Redraw" />
      <Area>
        <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
        ...
      </Area>
      ...
  </WidgetLook>
  ...
</Falagard>
```

<a id="fal_elem_ref_eventlinkdefintion"></a>
## \<EventLinkDefinition\> Element

<a id="fal_elem_ref_eventlinkdefintion_1"></a>
### Purpose:

The `<EventLinkDefinition>` element is used to define an event on a window using the `<WidgetLook>` being defined.  The new event can be linked to other events on the window, or to events on child windows.  For child windows, the window must exist, and the facility is largely intended to be able to link to events on windows defined via the `<Child>` element.

<a id="fal_elem_ref_eventlinkdefintion_2"></a>
### Attributes:

- `name` specifies the unique name to use for the new event.  Required attribute.
- `widget` specifies the name suffix of the child widget containing an event that will be linked to the new event being defined.  Optional attribute.
- `event` specifies the name of an event on widget identified via `widget` that is to be linked to the new event being defined. If this is omitted but `widget` is specified, it will be assumed that the event to link to has the same name as the event being defined. Optional attribute.

<a id="fal_elem_ref_eventlinkdefintion_3"></a>
### Usage:

- The `<EventLinkDefinition>` element may contain any number of `<EventLinkTarget>` sub-elements.
- The `<EventLinkDefinition>` element may only appear as a sub-element within `<WidgetLook>` elements.

<a id="fal_elem_ref_eventlinkdefintion_4"></a>
### Examples:

TODO

<a id="fal_elem_ref_eventlinktarget"></a>
## \<EventLinkTarget\> Element

<a id="fal_elem_ref_eventlinktarget_1"></a>
### Purpose:

The `<EventLinkTarget>` element specifies a target widget suffix and event name to be used with a `<EventLinkDefinition>.`  Whenever the event specified here fires, the event defined by the enclosing `<EventLinkDefinition>` will also fire.

<a id="fal_elem_ref_eventlinktarget_2"></a>
### Attributes:

- `widget` specifies the name suffix of the child widget containing an event that will be linked to the new event being defined by the enclosing `<EventLinkDefinition>.` Optional attribute.
- `event` specifies the name of an event on the widget identified via `widget` that is to be linked to the event being defined by the enclosing `<EventLinkDefinition>.` If this is omitted but `widget` is specified, it will be assumed that the event to link to has the same name as the event being defined. Optional attribute.

<a id="fal_elem_ref_eventlinktarget_3"></a>
### Usage:

- The `<EventLinkTarget>` element may not contain sub-elements.
- The `<EventLinkTarget>` element may only appear as a sub-element within `<EventLinkDefinition>` elements.

<a id="fal_elem_ref_eventlinktarget_4"></a>
### Examples:

TODO

<a id="fal_elem_ref_sec_11"></a>
## \<Falagard\> Element

<a id="fal_elem_ref_sec_11_1"></a>
### Purpose:

The `<Falagard>` element is the root element in Falagard XML skin definition files. The element serves mainly as a container for `<WidgetLook>` elements

<a id="fal_elem_ref_sec_11_2"></a>
### Attributes:

- `version`  specifies the version of the resource file. Should be specified for all files, current CEGUI falagard version is: 7

<a id="fal_elem_ref_sec_11_3"></a>
### Usage:

- The `<Falagard>` element is the root element for Falagard skin files.
- The `<Falagard>` element may contain any number of `<WidgetLook>` elements.
- No element may contain `<Falagard>` elements as a sub-element.

<a id="fal_elem_ref_sec_11_4"></a>
### Examples:

Here we just see the general structure of a Falagard XML file, notice that the `<Falagard>` element just serves as a container for multiple `<WidgetLook>` elements:

```xml
<?xml version="1.0" ?>
<Falagard>
  <WidgetLook name="TaharezLook/Button">
  ...
  </WidgetLook>
  <WidgetLook ... >
  ...
  </WidgetLook>
  ...
</Falagard>
```

<a id="fal_elem_ref_sec_12"></a>
## \<FontDim\> Element

<a id="fal_elem_ref_sec_12_1"></a>
### Purpose:

The `<FontDim>` element is used to take some measurement of a Font, and use it as a dimension component of an area rectangle.

<a id="fal_elem_ref_sec_12_2"></a>
### Attributes:

- `widget`  specifies the name suffix of a child window to access when automatically obtaining the font or text string to be used when calculating the dimension's value. The final name used to access the widget will be that of the target window with this suffix appended.  If this suffix is not specified, the target window itself is used. Optional attribute.
- `type`  specifies the type of font metric / measurement to use for this dimension. This should be set to one of the values from the FontMetricType enumeration. Required attribute.
- `font`  specifies the name of a font. If no font is given, the font will be taken from the target window at the time the dimension's value is taken. Optional attribute.
- `string`  For horizontal extents measurement, specifies the string to be measured. If no explicit string is given, the window text for the target window at the time the dimension's value is taken will be used instead. Optional attribute.
- `padding`  an absolute pixel 'padding' value to be added to the font metric value. Optional attribute.

<a id="fal_elem_ref_sec_12_3"></a>
### Usage:

- The `<FontDim>` element can appear as a sub-element in `<Dim>` to form a dimension specification for an area.
- The `<FontDim>` element can appear as a sub-element of `<OperatorDim>` to specify one of the operands for a dimension calculation.

<a id="fal_elem_ref_sec_12_4"></a>
### Examples:

This first example just gets the line spacing for the window's current font:

```xml
<Dim type="Height">
  <FontDim type="LineSpacing" />
</Dim>
```

Now we take an extents measurement of the windows current text, using a specified font, and pad the result by ten pixels:

```xml
<Dim type="Width">
  <FontDim type="HorzExtent" font="Roman-14" padding="10" />
</Dim>
```

<a id="fal_elem_ref_sec_13"></a>
## \<FontProperty\> Element

<a id="fal_elem_ref_sec_13_1"></a>
### Purpose:

The `<FontProperty>` element is intended to allow the system to access a property on the target window to obtain the font to be used when rendering the TextComponent being defined.

<a id="fal_elem_ref_sec_13_2"></a>
### Attributes:

- `name`  specifies the name of the property to access. Required attribute.  The value of the named property is taken as being the name of a Font.

<a id="fal_elem_ref_sec_13_3"></a>
### Usage:

- The `<FontProperty>` element may not contain sub-elements.
- The `<FontProperty>` element may appear as a sub-element only within the `<TextComponent>` element.

<a id="fal_elem_ref_sec_13_4"></a>
### Examples:

<a id="fal_elem_ref_sec_14"></a>
## \<FrameComponent\> Element

<a id="fal_elem_ref_sec_14_1"></a>
### Purpose:

The `<FrameComponent>` element is used to define an imagery frame using a maximum of eight images for the corners and edges, and a single, formatted, image for the background. Any of the images may be omitted if not required.

<a id="fal_elem_ref_sec_14_2"></a>
### Attributes:

No attributes are currently defined for the `<FrameComponent>` element.

<a id="fal_elem_ref_sec_14_3"></a>
### Usage:

Note: the sub-elements should appear in the order that they are defined here.

- `<Area>` defining the target area for this frame.
- Up to nine `<Image>` or `<ImageProperty>` elements specifying the images to be drawn and in what positions. Note that it is acceptable to freely mix `<Image>` and `<ImageProperty>` in a single `<FrameComponent>` definition.
- Optionally specifying the colours for the entire frame, one of the colour elements:
  - `<Colours>`
  - `<ColourProperty>`
  - `<ColourRectProperty>`
- Optionally, to specify the vertical formatting to use for the frame background, either of:
  - `<VertFormat>`
  - `<VertFormatProperty>`
- Optionally, to specify the horizontal formatting to use for the frame background, either of:
  - `<HorzFormat>`
  - `<HorzFormatProperty>`
- The `<FrameComponent>` element may only appear as a sub-element of the element `<ImagerySection>.`

<a id="fal_elem_ref_sec_14_4"></a>
### Examples:

The following defines a full frame and background. It is taken from the TaharezLook skin specification for the Listbox widget:

```xml
<FrameComponent>
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="Width" ><UnifiedDim scale="1" type="Width" /></Dim>
    <Dim type="Height" ><UnifiedDim scale="1" type="Height" /></Dim>
  </Area>
  <Image type="TopLeftCorner"
    imageset="TaharezLook" image="ListboxTopLeft"
  />
  <Image type="TopRightCorner"
    imageset="TaharezLook" image="ListboxTopRight"
  />
  <Image type="BottomLeftCorner"
    imageset="TaharezLook" image="ListboxBottomLeft"
  />
  <Image type="BottomRightCorner"
    imageset="TaharezLook" image="ListboxBottomRight"
  />
  <Image type="LeftEdge"
    imageset="TaharezLook" image="ListboxLeft"
  />
  <Image type="RightEdge"
    imageset="TaharezLook" image="ListboxRight"
  />
  <Image type="TopEdge"
    imageset="TaharezLook" image="ListboxTop"
  />
  <Image type="BottomEdge"
    imageset="TaharezLook" image="ListboxBottom"
  />
  <Image type="Background"
    imageset="TaharezLook" image="ListboxBackdrop"
  />
</FrameComponent>
```

<a id="fal_elem_ref_sec_15"></a>
## \<HorzAlignment\> Element

<a id="fal_elem_ref_sec_15_1"></a>
### Purpose:

The `<HorzAlignment>` element is used to specify the horizontal alignment option required for a child window element.

<a id="fal_elem_ref_sec_15_2"></a>
### Attributes:

- `type`  specifies one of the values from the HorizontalAlignment enumeration indicating the desired horizontal alignment.

<a id="fal_elem_ref_sec_15_3"></a>
### Usage:

- The `<HorzAlignment>` element may only appear as a sub-element of the `<Child>` element.
- The `<HorzAlignment>` element may not contain any sub-elements.

<a id="fal_elem_ref_sec_15_4"></a>
### Examples:

This example defines a scrollbar type child widget. We have used the `<HorzAlignment>` element to specify that the scrollbar appear on the far right edge of the component being defined:

```xml
...
<Child type="MyLook/VertScrollbar" nameSuffix="__auto_vscrollbar__">
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="Width" ><AbsoluteDim value="15" /></Dim>
    <Dim type="Height" ><UnifiedDim scale="1" type="Height" /></Dim>
  </Area>
  <HorzAlignment type="RightAligned" />
</Child>
...
```

<a id="fal_elem_ref_sec_16"></a>
## \<HorzFormat\> Element

<a id="fal_elem_ref_sec_16_1"></a>
### Purpose:

The `<HorzFormat>` element is used to specify the required horizontal formatting for an image, frame, or text component.

<a id="fal_elem_ref_sec_16_2"></a>
### Attributes:

- `type` specifies the required horizontal formatting option.
  - For use in ImageryComponents or FrameComponents, this will be one of the values from the HorizontalFormat enumeration.
  - For use in TextComponents, this will one of the values form the HorizontalTextFormat enumeration.
- `component` Only for FrameComponent. Specifies the part of the frame that this formatting is to be used for. Should be "TopEdge", "BottomEdge" or "Background" from the FrameImageComponent enumeration. Optional attribute, defaults to "Background".

<a id="fal_elem_ref_sec_16_3"></a>
### Usage:

- The `<HorzFormat>` element may only appear as a sub-element of the following elements:
  - `<ImageryComponent>`
  - `<FrameComponent>`
  - `<TextComponent>`
- The `<HorzFormat>` element may not contain any sub-elements.

<a id="fal_elem_ref_sec_16_4"></a>
### Examples:

This first example shows an ImageryComponent definition. We use `<HorzFormat>` to specify that we want the image stretched to cover the entire width of the designated target area:

```xml
...
<ImageryComponent>
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="Width" ><AbsoluteDim value="25" /></Dim>
    <Dim type="Height" ><AbsoluteDim value="25" /></Dim>
  </Area>
  <Image imageset="myImageset" image="coolImage" />
  <VertFormat type="Stretched" />
  <HorzFormat type="Stretched" />
</ImageryComponent>
...
```

This second example is for a TextComponent. You can see `<HorzFormat>` used here to specify that we want the text centred within the target area, and word-wrapped where required:

```xml
<TextComponent>
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="RightEdge" ><UnifiedDim scale="1" type="Width" /></Dim>
    <Dim type="Height" ><UnifiedDim scale="1" type="Height" /></Dim>
  </Area>
  <HorzFormat type="WordWrapLeftAligned" />
</TextComponent>
```

<a id="fal_elem_ref_sec_17"></a>
## \<HorzFormatProperty\> Element

<a id="fal_elem_ref_sec_17_1"></a>
### Purpose:

The `<HorzFormatProperty>` element is intended to allow the system to access a property on the target window to obtain the horizontal formatting to be used when drawing the component being defined.

<a id="fal_elem_ref_sec_17_2"></a>
### Attributes:

- `name`  specifies the name of the property to access. The named property must access a string value that will be set to one of the enumeration values appropriate for the component being defined (HorizontalTextFormat for TextComponent, and HorizontalFormat for either FrameComponent or ImageryComponent). Required attribute.
- `component`  Only for FrameComponent. Specifies the part of the frame that this formatting is to be used for. Should be "TopEdge", "BottomEdge" or "Background" from the FrameImageComponent enumeration. Optional attribute, defaults to "Background".

<a id="fal_elem_ref_sec_17_3"></a>
### Usage:

- The `<HorzFormatProperty>` element may not contain sub-elements.
- The `<HorzFormatProperty>` element may appear as a sub-element within any of the following elements:
  - `<ImageryComponent>` to specify a horizontal formatting to be used the the image.
  - `<FrameComponent>` to specify a horizontal formatting to be used for the frame background.
  - `<TextComponent>` to specify a horizontal formatting to be used for the text.

<a id="fal_elem_ref_sec_17_4"></a>
### Examples:

<a id="fal_elem_ref_sec_18"></a>
## \<Image\> Element

<a id="fal_elem_ref_sec_18_1"></a>
### Purpose:

The `<Image>` element is used to specify an Imageset and Image pair, and for FrameComponent images, how the image is to be used.

<a id="fal_elem_ref_sec_18_2"></a>
### Attributes:

- `imageset`  specifies the name of an Imageset which contains the image to be used. Required attribute.
- `image`  specifies the name of the image from the specified Imageset to be used. Required attribute.
- `component`  Only for FrameComponent. Specifies the part of the frame that this image is to be used for. One of the values from the FrameImageComponent enumeration. Required attribute.

<a id="fal_elem_ref_sec_18_3"></a>
### Usage:

- The `<Image>` element may only appear as a sub-element of the `<ImageryComponent>` or `<FrameComponent>` elements.
- The `<Image>` element may not contain any sub-elements.

<a id="fal_elem_ref_sec_18_4"></a>
### Examples:

Here you can see the `<Image>` element used to specify the image to render for an ImageryComponent being defined:

```xml
...
<ImageryComponent>
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="Width" ><AbsoluteDim value="15" /></Dim>
    <Dim type="Height" ><UnifiedDim scale="1.0" type="Height" /></Dim>
  </Area>
  <Image imageset="FunkyLook" image="ButtonIcon" />
  <VertFormat type="CentreAligned" />
  <HorzFormat type="CentreAligned" />
</ImageryComponent>
...
```

<a id="fal_elem_ref_sec_19"></a>
## \<ImageDim\> Element

<a id="fal_elem_ref_sec_19_1"></a>
### Purpose:

The `<ImageDim>` element is used to define a component dimension for an area rectangle. `<ImageDim>` is used to specify some dimension of an image for use as an area dimension.

<a id="fal_elem_ref_sec_19_2"></a>
### Attributes:

- `name`  specifies the name of the image to be used. Required attribute.
- `dimension`  specifies the image dimension to be used. This should be set to one of the values defined in the DimensionType enumeration. Required attribute.

<a id="fal_elem_ref_sec_19_3"></a>
### Usage:

- The `<ImageDim>` element can appear as a sub-element in `<Dim>` to form a dimension specification for an area.
- The `<ImageDim>` element can appear as a sub-element of `<OperatorDim>` to specify one of the operands for a dimension calculation.

<a id="fal_elem_ref_sec_19_4"></a>
### Examples:

This example shows a dimension that uses `<ImageDim>` to fetch the width of a specified image for use as the dimensions value:

```xml
...
<Area>
  <Dim type="LeftEdge">
    <ImageDim name="myImages/leftImage" dimension="Width" />
  </Dim>
  ...
</Area>
...
```

<a id="fal_elem_ref_sec_imagepropertydim"></a>
## \<ImagePropertyDim\> Element

<a id="fal_elem_ref_sec_imagepropertydim_1"></a>
### Purpose:

The `<ImagePropertyDim>` element is used to define a component dimension for an area rectangle. `<ImagePropertyDim>` is used to specify some dimension of an image that is named by a property for use as an area dimension.

<a id="fal_elem_ref_sec_imagepropertydim_2"></a>
### Attributes:

- `name`  specifies the name of the property that will fetch the name of the Image to be used. Required attribute.
- `dimension`  specifies the image dimension to be used. This should be set to one of the values defined in the DimensionType enumeration. Required attribute.

<a id="fal_elem_ref_sec_imagepropertydim_3"></a>
### Usage:

- The `<ImagePropertyDim>` element can appear as a sub-element in `<Dim>` to form a dimension specification for an area.
- The `<ImagePropertyDim>` element can appear as a sub-element of `<OperatorDim>` to specify one of the operands for a dimension calculation.

<a id="fal_elem_ref_sec_imagepropertydim_4"></a>
### Examples:

This example shows a dimension that uses `<ImagePropertyDim>` to fetch the Height of the image specified in the property `FrameTopImage` for use as the dimension's value:

```xml
...
<Area>
  <Dim type="TopEdge">
    <ImagePropertyDim name="FrameTopImage" dimension="Height" />
  </Dim>
  ...
</Area>
...
```

<a id="fal_elem_ref_sec_20"></a>
## \<ImageryComponent\> Element

<a id="fal_elem_ref_sec_20_1"></a>
### Purpose:

The `<ImageryComponent>` element defines a single image to be drawn within a given ImagerySection. The ImageryComponent contains all information about which image is to be drawn, where it should be drawn, which colours are to be used and how the image should be formatted.

<a id="fal_elem_ref_sec_20_2"></a>
### Attributes:

No attributes are defined for the `<ImageryComponent>` element.

<a id="fal_elem_ref_sec_20_3"></a>
### Usage:

Note: the sub-elements should appear in the order that they are defined here.

- `<Area>` defining the target area for this image.
- Either one of:
  - `<Image>` element specifying the image to be drawn.
  - `<ImageProperty>` element specifying a property defining the image to be drawn.
- Optionally specifying the colours for this single image, one of the colour elements:
  - `<Colours>`
  - `<ColourProperty>`
  - `<ColourRectProperty>`
- Optionally, to specify the vertical formatting to use, either of:
  - `<VertFormat>`
  - `<VertFormatProperty>`
- Optionally, to specify the horizontal formatting to use, either of:
  - `<HorzFormat>`
  - `<HorzFormatProperty>`
- The `<ImageryComponent>` element may only appear as a sub-element of the element `<ImagerySection>.`

<a id="fal_elem_ref_sec_20_4"></a>
### Examples:

The following was taken from TaharezLook.looknfeel and shows a full ImageryComponent definition:

```xml
<ImageryComponent>
  <Area>
    <Dim type="LeftEdge" ><UnifiedDim scale="0" type="LeftEdge" /></Dim>
    <Dim type="TopEdge" ><UnifiedDim scale="0.2" type="TopEdge" /></Dim>
    <Dim type="Width" ><UnifiedDim scale="1" type="Width" /></Dim>
    <Dim type="Height" ><UnifiedDim scale="0.3" type="Height" /></Dim>
  </Area>
  <Image imageset="TaharezLook" image="TextSelectionBrush" />
  <Colours
    topLeft="FFFFFF00"
    topRight="FFFFFF00"
    bottomLeft="FFFFFF00"
    bottomRight="FFFFFF00"
  />
  <VertFormat type="Tiled" />
  <HorzFormat type="Stretched" />
</ImageryComponent>
```

<a id="fal_elem_ref_sec_21"></a>
## \<ImageProperty\> Element

<a id="fal_elem_ref_sec_21_1"></a>
### Purpose:

The `<ImageProperty>` element is intended to allow the system to access a property on the target window to obtain the final image to be used when rendering the component being defined.

<a id="fal_elem_ref_sec_21_2"></a>
### Attributes:

- `name`  specifies the name of the property to access that will provide the name of the Image to be used. Required attribute.
- `component`  Only for `<FrameComponent>.` Specifies the part of the frame that this image is to be used for. One of the values from the FrameImageComponent enumeration. Required attribute.

<a id="fal_elem_ref_sec_21_3"></a>
### Usage:

- The `<ImageProperty>` element may not contain sub-elements.
- The `<ImageProperty>` element may appear as a sub-element within either `<ImageryComponent>` or `<FrameComponent>` elements.

<a id="fal_elem_ref_sec_21_4"></a>
### Examples:

<a id="fal_elem_ref_sec_22"></a>
## \<ImagerySection\> Element

<a id="fal_elem_ref_sec_22_1"></a>
### Purpose:

The `<ImagerySection>` element is used to group multiple `<ImageryComponent>` and `<TextComponent>` definitions into named sections which can then be specified for use as imagery in state definitions.

<a id="fal_elem_ref_sec_22_2"></a>
### Attributes:

- `name`  specifies the name to be given to this ImagerySection. Names are per-WidgetLook, and specifying the same name more than once will replace the previous definition. Required attribute.

<a id="fal_elem_ref_sec_22_3"></a>
### Usage:

Note: the sub-elements should appear in the order that they are defined here.

- To optionally specify colours to be modulated with the individual component's colours, the `<ImagerySection>` may contain one of the colour definition elements:
  - `<Colours>`
  - `<ColourProperty>`
  - `<ColourRectProperty>`
- Any number of `<FrameComponent>` elements may then follow.
- Followed by any number of `<ImageryComponent>` elements.
- Finally, any number of `<TextComponent>` elements may be given.
- The `<ImagerySection>` element may only appear as a sub-element of the `<WidgetLook>` element.

<a id="fal_elem_ref_sec_22_4"></a>
### Examples:

```xml
<ImagerySection name="example">
  <ImageryComponent>
    <Area>
      <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
      <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
      <Dim type="Width" ><AbsoluteDim value="15" /></Dim>
      <Dim type="Height" ><UnifiedDim scale="1.0" type="Height" /></Dim>
    </Area>
    <Image imageset="sillyImages" image="anotherImage" />
    <VertFormat type="Stretched" />
    <HorzFormat type="Stretched" />
  </ImageryComponent>
  <TextComponent>
    <Area>
      <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
      <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
      <Dim type="Width" ><UnifiedDim scale="1" type="Width" /></Dim>
      <Dim type="Height" ><UnifiedDim scale="1" type="Height" /></Dim>
    </Area>
  </TextComponent>
</ImagerySection>
```

<a id="fal_elem_ref_sec_23"></a>
## \<Layer\> Element

<a id="fal_elem_ref_sec_23_1"></a>
### Purpose:

The `<Layer>` element is used to define layers of imagery within the definition of a StateImagery section.

<a id="fal_elem_ref_sec_23_2"></a>
### Attributes:

- `priority`  specifies the priority for the layer. Higher priorities appear in front of lower priorities. Default priority is 0. Optional attribute.

<a id="fal_elem_ref_sec_23_3"></a>
### Usage:

- The `<Layer>` element may only appear as a sub-element of the `<StateImagery>` element.
- The `<Layer>` element may contain any number of `<Section>` sub-elements.

<a id="fal_elem_ref_sec_23_4"></a>
### Examples:

Here we see a single layer with multiple sections included. This example was taken from the TaharezLook skin XML file (ListHeaderSegment widget):

```xml
<StateImagery name="Normal">
  <Layer>
    <Section section="segment_normal" />
    <Section section="splitter_normal" />
    <Section section="label" />
  </Layer>
</StateImagery>
```

<a id="fal_elem_ref_sec_24"></a>
## \<NamedArea\> Element

<a id="fal_elem_ref_sec_24_1"></a>
### Purpose:

Defines an area that can be accessed via it's name. Generally this this used by base widgets to obtain skin supplied areas for use in rendering or other widget specific operations.

<a id="fal_elem_ref_sec_24_2"></a>
### Attributes:

- `name`  specifies a name for the area being defined. Required attribute.

<a id="fal_elem_ref_sec_24_3"></a>
### Usage:

- The `<NamedArea>` element must contain only an `<Area>` sub-element defining the area rectangle for the named area.
- The `<NamedArea>` element may only appear as a sub-element within `<WidgetLook>` elements.

<a id="fal_elem_ref_sec_24_4"></a>
### Examples:

This example defines a named area called 'TextArea'. It is defined as being an area seven pixels inside the total area of the widget being defined:

```xml
<NamedArea name="TextArea">
  <Area>
    <Dim type="LeftEdge" >
      <AbsoluteDim value="7" />
    </Dim>
    <Dim type="TopEdge" >
      <AbsoluteDim value="7" />
    </Dim>
    <Dim type="RightEdge" >
      <UnifiedDim scale="1.0" offset="-7" type="RightEdge" />
    </Dim>
    <Dim type="BottomEdge" >
      <UnifiedDim scale="1.0" offset="-7" type="BottomEdge" />
    </Dim>
  </Area>
</NamedArea>
```

<a id="fal_elem_ref_sec_operatordim"></a>
## \<OperatorDim\> Element

<a id="fal_elem_ref_sec_operatordim_1"></a>
### Purpose:

The `<OperatorDim>` element allows you to use the result of performing a mathematical calculation on two two dimension elements. Since either dimension used as operands may also be an `<OperatorDim>` it is possible to create expression trees to perform any mathematical calculation that can be expressed using the supported operators.

<a id="fal_elem_ref_sec_operatordim_2"></a>
### Attributes:

- `op`  specifies one of the vales from the DimensionOperator enumeration indicating the mathematical operation to be performed. Required attribute.

<a id="fal_elem_ref_sec_operatordim_3"></a>
### Usage:

- A single `<OperatorDim>` element may appear as a sub-element within the following:
  - `<Dim>`
  - `<OperatorDim>`
- The `<OperatorDim>` element must contain any of two the following dimension elements:
  - `<AbsoluteDim>`
  - `<FontDim>`
  - `<ImageDim>`
  - `<ImagePropertyDim>`
  - `<PropertyDim>`
  - `<UnifiedDim>`
  - `<WidgetDim>`
  - `<OperatorDim>`

<a id="fal_elem_ref_sec_operatordim_4"></a>
### Examples:

The following multiplies two simple AbsoluteDim dimensions:

```xml
...
<OperatorDim op="Multiply">
  <AbsoluteDim value="10" />
  <AbsoluteDim value="4" />
</OperatorDim>
...
```

The next example takes the height of the font used for the target window, adds four pixels and multiplies the result by two.

The operation performed will be:

```text
(LineSpacing + 4) * 2
```

```xml
...
<OperatorDim op="Multiply">
  <OperatorDim op="Add">
    <FontDim type="LineSpacing" />
    <AbsoluteDim value="4" />
  </OperatorDim>
  <AbsoluteDim value="2" />
</OperatorDim>
...
```

<a id="fal_elem_ref_sec_25"></a>
## \<Property\> Element

<a id="fal_elem_ref_sec_25_1"></a>
### Purpose:

The `<Property>` element is used to initialise a property on a window or widget being defined.

<a id="fal_elem_ref_sec_25_2"></a>
### Attributes:

- `name`  specifies the name of the property to be initialised. Required attribute.
- `value`  specifies the value string to be used when initialising the property. Required attribute.

<a id="fal_elem_ref_sec_25_3"></a>
### Usage:

- The `<Property>` element may not contain any sub-elements.
- The `<Property>` element may appear as a sub-element in `<WidgetLook>` elements to define property initialisers for the type being defined.
- The `<Property>` element may appear as a sub-element in `<Child>` elements to define property initialisers for the child widget being defined.

<a id="fal_elem_ref_sec_25_4"></a>
### Examples:

In this extract from the definition for TaharezLook/Titlebar, we can see the `<Property>` element used to set the 'CaptionColour' property; this establishes a default for all instances of this widget:

```xml
<WidgetLook name="TaharezLook/Titlebar">
  <Property name="CaptionColour" value="FFFFFFFF" />
  <ImagerySection name="main">
    <ImageryComponent>
      <Area>
        <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
        ...
      </Area>
      ...
    </ImageryComponent>
  </ImagerySection>
  ...
</WidgetLook>
```

<a id="fal_elem_ref_sec_26"></a>
## \<PropertyDefinition\> Element

<a id="fal_elem_ref_sec_26_1"></a>
### Purpose:

The `<PropertyDefinition>` element creates a new named property for the widget being defined. The defined property may be accessed via any means that a 'normal' property may.

<a id="fal_elem_ref_sec_26_2"></a>
### Attributes:

- `name`  specifies the name to use for the new property. Required attribute.
- `initialValue`  specifies the initial value to be assigned to the property. Optional attribute.
- `type`  specifies the data type of the property. This should be one of the values defined for the PropertyType enumeration. Defaults to `Generic.` Optional attribute.
- `redrawOnWrite`  boolean setting specifies whether writing a new value to this property should cause the widget being defined to redraw itself. Optional attribute.
- `layoutOnWrite`  boolean setting specifies whether writing a new value to this property should cause the widget being defined to re-layout it's defined child widgets. Optional attribute.
- `fireEvent`  specifies the name of an event to fire when this property is written to. The event is passed a CEGUI::WindowEventArgs reference with the window field initialised to the window upon which the property was written. For the CEGUI::GlobalEventSet, the event uses the name of the WidgetLook being defined as the event namespace. Optional attribute.

<a id="fal_elem_ref_sec_26_3"></a>
### Usage:

- The `<PropertyDefinition>` element may not contain sub-elements.
- The `<PropertyDefinition>` element must appear as a sub-element within `<WidgetLook>` elements.

<a id="fal_elem_ref_sec_26_4"></a>
### Examples:

In this example, within the WidgetLook we create a new property named 'ScrollbarWidth'. We then use this property to control the width of a component child widget. This effectively gives the user control over the width of the child scrollbar via the property:

```xml
<WidgetLook name="PropertyDefExample">
  <PropertyDefinition
    name="ScrollbarWidth"
    initialValue="12"
    layoutOnWrite="true"
  />
  ...
  <Child type="MyVertScrollbar" nameSuffix="__auto_vscrollbar__">
    <Area>
      <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
      <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
      <Dim type="Width" ><PropertyDim name="ScrollbarWidth" /></Dim>
      <Dim type="Height" ><UnifiedDim scale="1" type="Height" /></Dim>
    </Area>
    <HorzAlignment type="RightAligned" />
  </Child>
  ...
</WidgetLook>
```

<a id="fal_elem_ref_sec_27"></a>
## \<PropertyLinkDefinition\> Element

<a id="fal_elem_ref_sec_27_1"></a>
### Purpose:

The `<PropertyLinkDefinition>` element creates a new named property for the widget being defined that is linked to one or more properties on either child widget components, or on the parent widget.  The target widgets and properties can be specified either as attributes (for example if the link is to be a one to one mapping), or via \<PropertyLinkTarget\> elements (if there is to be a one to many mapping).  This allows properties on child widgets to be directly exposed to clients of the widget being defined, as well as allowing the widget being defined to make use of properties defined on a parent widget.  The defined property may be accessed via any means that a 'normal' property may.

<a id="fal_elem_ref_sec_27_2"></a>
### Attributes:

- `name`  specifies the name to use for the new property. Required attribute.
- `widget`  specifies either the name suffix of the child widget containing the first property to be linked to the property being defined, or the special value `"__parent__"` to indicate a back-link to the parent. Optional attribute.
- `targetProperty`  specifies the name of the property on the child widget that is to be the first property linked to the new property being defined. If this is omitted but `widget` is specified, it will be assumed that the target property has the same name as the property being defined. Optional attribute.
- `initialValue`  specifies the initial value to be assigned to the property. Optional attribute.
- `type`  specifies the data type of the property. This should be one of the values defined for the PropertyType enumeration. Defaults to `Generic.` Optional attribute.
- `redrawOnWrite`  boolean setting specifies whether writing a new value to this property should cause the widget being defined to redraw itself. Optional attribute.
- `layoutOnWrite`  boolean setting specifies whether writing a new value to this property should cause the widget being defined to re-layout it's defined child widgets. Optional attribute.
- `fireEvent`  specifies the name of an event to fire when this property is written to. The event is passed a CEGUI::WindowEventArgs reference with the window field initialised to the window upon which the property was written. For the CEGUI::GlobalEventSet, the event uses the name of the WidgetLook being defined as the event namespace. It is the responsibility of the WidgetLook author to ensure that collisions with predefined events are avoided. Optional attribute.

<a id="fal_elem_ref_sec_27_3"></a>
### Usage:

- The `<PropertyLinkDefinition>` element may contain any number of `<PropertyLinkTarget>` sub-elements.
- The `<PropertyLinkDefinition>` element may only appear as a sub-element within `<WidgetLook>` elements.

<a id="fal_elem_ref_sec_27_4"></a>
### Examples:

In this example we create a new property named 'CaptionTextColour'.  This is linked to a property named 'CaptionColour' on the child widget with name suffix '__auto_titlebar__'. Any access of the 'CaptionTextColour' property on the widget will actually access the 'CaptionColour' property on the specified child widget:

```xml
<WidgetLook name="PropertyLinkExample">
  <PropertyLinkDefinition
    name="CaptionTextColour"
    widget="__auto_titlebar__"
    targetProperty="CaptionColour"
    initialValue="FFFF3333"
    layoutOnWrite="true"
  />
  ...
</WidgetLook>
```

<a id="fal_elem_propertylinktarget"></a>
## \<PropertyLinkTarget\> Element

<a id="fal_elem_propertylinktargetr_1"></a>
### Purpose:

The `<PropertyLinkTarget>` element specifies a target widget suffix and property name to be used with a `<PropertyLinkDefinition>.`  Whenever the property defined by the enclosing `<PropertyLinkDefinition>` is written to, the property specified in the `<PropertyLinkTarget>` will be written also. If the `<PropertyLinkTarget>` is the first linked target it will also be used as the 'master linked target' and will be used as the source for read accesses to the property defined by the enclosing `<PropertyLinkDefinition>` element.

<a id="fal_elem_propertylinktarget_2"></a>
### Attributes:

- `widget` specifies either the name suffix of the child widget containing the property that is to be linked to the property being defined by the enclosing `<PropertyLinkDefinition>` element, or the special value `"__parent__"` to indicate a back-link to the parent. Required attribute.
- `property` specifies the name of the property on the child widget that is to be linked to the property being defined by the enclosing `<PropertyLinkDefinition>.` If this is omitted, it will be assumed that the target property has the same name as the property being defined. Optional attribute.

<a id="fal_elem_propertylinktarget_3"></a>
### Usage:

- The `<PropertyLinkTarget>` element may not contain sub-elements.
- The `<PropertyLinkTarget>` element may only appear as a sub-element within `<PropertyLinkDefinition>` elements.

<a id="fal_elem_propertylinktarget_4"></a>
### Examples:

In this example we create a new property named 'TextColour'.  This is linked to separate properties on two different child components.  A property named 'LabelColour' on a child widget with name suffix '__auto_button1__', and a property named 'ContentColour' on a child widget with name suffix '__auto_content_panel__.  Writing to the property 'TextColour' will cause both 'LabelColour' and 'ContentColour' to be updated, while reading the property 'TextColour' will fetch the value of 'LabelColour' (because it appears first, it is treated as the master target).

```xml
<WidgetLook name="PropertyLinkTargetExample">
  <PropertyLinkDefinition name="TextColour" initialValue="FFFF00FF" >
    <PropertyLinkTarget widget="__auto_button1__" property="LabelColour" />
    <PropertyLinkTarget widget="__auto_content_panel__" property="ContentColour" />
  </PropertyLinkDefinition>
  ...
</WidgetLook>
```

<a id="fal_elem_ref_sec_28"></a>
## \<PropertyDim\> Element

<a id="fal_elem_ref_sec_28_1"></a>
### Purpose:

The `<PropertyDim>` element is used to define a component dimension for an area rectangle. `<PropertyDim>` is used to specify either a UDim or a simple floating point value - accessed via a window property - for use as an area dimension.

<a id="fal_elem_ref_sec_28_2"></a>
### Attributes:

- `widget`  specifies the name suffix of a child window to access the property for. The final name used to access the widget will be that of the target window with this suffix appended. If this suffix is not specified, the target window itself is used. Optional attribute.
- `name`  specifies the name of the property that will provide the value for this dimension. The property named should access either a UDim value or a simple floating point numerical value - the system determines which type of value to expect based upon the usage (or not) of the optional `type` attribute.
- `type` specifies the dimension for which the relative scale value of a UDim value is a portion of, and as such should be set to either `"Width"` or `"Height".`  If the property specified by the attribute `name` is intended to access a simple floating point value rather than a UDim value, this attribute should be omitted. Optional attribute.

<a id="fal_elem_ref_sec_28_3"></a>
### Usage:

- The `<PropertyDim>` element can appear as a sub-element in `<Dim>` to form a dimension specification for an area.
- The `<PropertyDim>` element can appear as a sub-element of `<OperatorDim>` to specify one of the operands for a dimension calculation.

<a id="fal_elem_ref_sec_28_4"></a>
### Examples:

This example shows a dimension that uses `<PropertyDim>` to fetch a property value to use as the dimension value. We are accessing the 'AbsoluteWidth' property, from an attached widget with the name suffix '__auto_button__', that accesses a simple floating point value:

```xml
...
<Area>
  <Dim type="LeftEdge">
    <PropertyDim widget="__auto_button__" name="AbsoluteWidth" />
  </Dim>
  ...
</Area>
...
```

Here we show a dimension that uses `<PropertyDim>` to access a property named 'UserWidth' on the target window.  We have specified the `type` attribute to be 'Width', which indicates to the system that the property will access a UDim value and that the scale part of the UDim is relative to the width of the target window.

```xml
...
<Area>
  ...
  <Dim type="Width">
    <PropertyDim name="UserWidth" type="Width" />
  </Dim>
  ...
</Area>
...
```

<a id="fal_elem_ref_sec_29"></a>
## \<Section\> Element

<a id="fal_elem_ref_sec_29_1"></a>
### Purpose:

The `<Section>` element is used to name an ImagerySection to be included for rendering within a StateImagery Layer definition.

<a id="fal_elem_ref_sec_29_2"></a>
### Attributes:

- `look`  specifies the name of a WidgetLook that contains the ImagerySection to be referenced. If this is omitted, the WidgetLook currently being defined is used. Optional attribute.
- `section`  specifies the name of an ImagerySection from the chosen WidgetLook to be referenced. Required attribute.
- `controlProperty`  specifies the name of a property that will be accessed to determine whether or not to render this section (see `controlValue` below for details of how it is determined whether or not the secion will be drawn). Optional attribute.
- `controlValue`  specifies a value that will be compared to the value fetched from `controlProperty` in order to decide whether to draw the section. If `controlValue` is not specified, or is specified as the empty string, then the property named in `controlProperty` is treated as a boolean value. Otherwise the value fetched from the property named in `controlPropery` must exactly match the value specified in `controlValue` for the imagery section to be drawn. Optional attribute.
- `controlWidget`  specifies either the name suffix of a child widget, or the special value `"__parent__",` to indicate a widget that will be used as the source of the property named in `controlProperty.`  If `controlWidget` is not specified, or is specified as the empty string, then the widget with WidgetLook assigned to it will be used as the source (matching the previous / default behaviour).  Optional attribute.

<a id="fal_elem_ref_sec_29_3"></a>
### Usage:

- The `<Section>` element may only appear as a sub-element within the `<Layer>` element.
- The `<Section>` element may specify colours to be modulated with any current colours used for each component within the named ImagerySection, by optionally specifying one of the colour elements as a sub-element:
  - `<Colours>`
  - `<ColourProperty>`
  - `<ColourRectProperty>`

<a id="fal_elem_ref_sec_29_4"></a>
### Examples:

Here we see a state definition from a button widget. The state specifies to use the 'normal' imagery section, and also the 'label' imagery section. The 'label' section is only drawn if the 'DrawText' property of the target window is 'True'. Colours for 'label' will be modulated with the colour obtained from the 'NormalTextColour' property of the target window:

```xml
...
<StateImagery name="Normal">
  <Layer>
    <Section section="normal" />
    <Section section="label" controlProperty="DrawText">
      <ColourProperty name="NormalTextColour" />
    </Section>
  </Layer>
</StateImagery>
...
```

<a id="fal_elem_ref_sec_30"></a>
## \<StateImagery\> Element

<a id="fal_elem_ref_sec_30_1"></a>
### Purpose:

The `<StateImagery>` element defines imagery to be used when rendering a named state. The base widget type intended as a target for the WidgetLook being defined will specify which states are required to be defined.

<a id="fal_elem_ref_sec_30_2"></a>
### Attributes:

- `name`  specifies the name of the state being defined. Required attribute.
- `clipped`  boolean setting that states whether imagery defined within this state should be clipped to the target window's defined area.  If this is specified and set to false, the state imagery will only be clipped to the display area. Optional attribute.

<a id="fal_elem_ref_sec_30_3"></a>
### Usage:

- The `<StateImagery>element` may contain any number of `<Layer>` sub-elements.
- The `<StateImagery>` element may only appear as a sub-element of the `<WidgetLook>` element.

<a id="fal_elem_ref_sec_30_4"></a>
### Examples:

The following is an extract of the MenuItem definition from TaharezLook.looknfeel.  The except defines some of the states required for that widget. Note that, although not shown here, a required state can be empty if no rendering is needed for that state:

```xml
...
<StateImagery name="EnabledNormal">
  <Layer>
    <Section section="label" />
  </Layer>
</StateImagery>
<StateImagery name="EnabledHover">
  <Layer>
    <Section section="frame" />
    <Section section="label" />
  </Layer>
</StateImagery>
<StateImagery name="EnabledPushed">
  <Layer>
    <Section section="frame" />
    <Section section="label" />
  </Layer>
</StateImagery>
...
```

<a id="fal_elem_ref_sec_31"></a>
## \<Text\> Element

<a id="fal_elem_ref_sec_31_1"></a>
### Purpose:

The `<Text>` element is used to define font and text string information within a TextComponent.

<a id="fal_elem_ref_sec_31_2"></a>
### Attributes:

- `font`  specifies the name of a font to use for this text. If this is omitted, the current font of the target window will be used instead.  Optional attribute.
- `string`  specifies a text string to be rendered. If this is omitted, the current window text for the target window will be used instead.  Optional attribute.

<a id="fal_elem_ref_sec_31_3"></a>
### Usage:

- The `<Text>` element may not contain any sub-elements.
- The `<Text>` element should only appear as a sub-element within `<TextComponent>` elements.

<a id="fal_elem_ref_sec_31_4"></a>
### Examples:

In this simple example, we define a TextComponent that renders some static text. The `<Text>` element is used to specify the font and string to be used:

```xml
...
<TextComponent>
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="Width" ><UnifiedDim scale="1" type="Width" /></Dim>
    <Dim type="Height" ><UnifiedDim scale="1" type="Height" /></Dim>
  </Area>
  <Text font="Roman-18" string="Render this text!" />
</TextComponent>
...
```

<a id="fal_elem_ref_sec_32"></a>
## \<TextComponent\> Element

<a id="fal_elem_ref_sec_32_1"></a>
### Purpose:

The `<TextComponent>` element defines a single item of text to be drawn within a given ImagerySection. The TextComponent contains all information about the text that is to be drawn, where it should be drawn, which colours are to be used and how the text should be formatted within its area.

Note that if the `<Text>` element appears in addition to either of the `<TextProperty>` or `<FontProperty>` elements, the string and font specified within the `<Text>` element will act as default values if the properties referenced in `<TextProperty>` or `<FontProperty>` evaluate to empty strings.

<a id="fal_elem_ref_sec_32_2"></a>
### Attributes:

The `<TextComponent>` element has no attributes defined.

<a id="fal_elem_ref_sec_32_3"></a>
### Usage:

Note: the sub-elements should appear in the order that they are defined here.

- `<Area>` defining the target area for the text.
- `<Text>` optional element specifying the font to be used and text string to be drawn.
- `<TextProperty>` optional element specifying the name of a property that contains the text to be drawn.
- `<FontProperty>` optional element specifying the name of a property that contains the name of the font to use when drawing the text.
- Optionally specifying the colours for this text, one of the colour elements:
  - `<Colours>`
  - `<ColourProperty>`
  - `<ColourRectProperty>`
- Optionally, to specify the vertical formatting to use, either of:
  - `<VertFormat>`
  - `<VertFormatProperty>`
- Optionally, to specify the horizontal formatting to use, either of:
  - `<HorzFormat>`
  - `<HorzFormatProperty>`
- The `<TextComponent>` element may only appear as a sub-element of the element `<ImagerySection>.`

<a id="fal_elem_ref_sec_32_4"></a>
### Examples:

The following example could be used to specify the caption text to appear within a Titlebar style widget:

```xml
...
<ImagerySection name="caption">
  <TextComponent>
    <Area>
      <Dim type="LeftEdge" ><AbsoluteDim value="10" /></Dim>
      <Dim type="TopEdge" ><AbsoluteDim value="2" /></Dim>
      <Dim type="Width" ><UnifiedDim scale="1" type="Width" /></Dim>
      <Dim type="Height" ><UnifiedDim scale="1" type="Height" /></Dim>
    </Area>
    <ColourProperty name="CaptionColour" />
    <VertFormat type="CentreAligned" />
    <HorzFormat type="WordWrapLeftAligned" />
  </TextComponent>
</ImagerySection>
...
```

<a id="fal_elem_ref_sec_33"></a>
## \<TextProperty\> Element

<a id="fal_elem_ref_sec_33_1"></a>
### Purpose:

The `<TextProperty>` element is intended to allow the system to access a property on the target window to obtain the text to be used when rendering the TextComponent being defined.

<a id="fal_elem_ref_sec_33_2"></a>
### Attributes:

- `name` specifies the name of the property to access.  The value of the named property is taken as a string to be rendered.  Required attribute.

<a id="fal_elem_ref_sec_33_3"></a>
### Usage:

- The `<TextProperty>` element may not contain sub-elements.
- The `<TextProperty>` element may appear as a sub-element only within the `<TextComponent>` element.

<a id="fal_elem_ref_sec_33_4"></a>
### Examples:

<a id="fal_elem_ref_sec_34"></a>
## \<UnifiedDim\> Element

<a id="fal_elem_ref_sec_34_1"></a>
### Purpose:

The `<UnifiedDim>` element is used to define a component dimension for an area rectangle. `<UnifiedDim>` is used to specify a value using the 'unified' co-ordinate system.

<a id="fal_elem_ref_sec_34_2"></a>
### Attributes:

- `scale` specifies the relative scale component of the UDim. Optional attribute.
- `offset` specifies the absolute pixel component of the UDim. Optional attribute.
- `type`  specifies what the dimension represents. This is needed so that the system knows how to interpret the 'scale' component.  Required attribute.

<a id="fal_elem_ref_sec_34_3"></a>
### Usage:

- The `<UnifiedDim>` element can appear as a sub-element in `<Dim>` to form a dimension specification for an area.
- The `<UnifiedDim>` element can appear as a sub-element of `<OperatorDim>` to specify one of the operands for a dimension calculation.

<a id="fal_elem_ref_sec_34_4"></a>
### Examples:

This example shows a dimension that uses `<UnifiedDim>` to specify a UDim value to use as the dimension's value:

```xml
...
<Area>
  <Dim type="LeftEdge">
    <UnfiedDim scale="0.5" offset="-8" type="LeftEdge" />
  </Dim>
  ...
</Area>
...
```

<a id="fal_elem_ref_sec_35"></a>
## \<VertAlignment\> Element

<a id="fal_elem_ref_sec_35_1"></a>
### Purpose:

The `<VertAlignment>` element is used to specify the vertical alignment option required for a child window element.

<a id="fal_elem_ref_sec_35_2"></a>
### Attributes:

- `type`  specifies one of the values from the VerticalAlignment enumeration indicating the desired vertical alignment.

<a id="fal_elem_ref_sec_35_3"></a>
### Usage:

- The `<VertAlignment>` element may only appear as a sub-element of the `<Child>` element.
- The `<VertAlignment>` element may not contain any sub-elements.

<a id="fal_elem_ref_sec_35_4"></a>
### Examples:

This example defines a scrollbar type child widget. We have used the `<VertAlignment>` element to specify that the scrollbar appear on the bottom edge of the component being defined:

```xml
...
<Child type="MyLook/HorzScrollbar" nameSuffix="__auto_hscrollbar__">
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="Width" ><UnifiedDim scale="1" type="Width? /></Dim>
    <Dim type="Height" ><AbsoluteDim value="15" /></Dim>
  </Area>
  <VertAlignment type="BottomAligned" />
</Child>
...
```

<a id="fal_elem_ref_sec_36"></a>
## \<VertFormat\> Element

<a id="fal_elem_ref_sec_36_1"></a>
### Purpose:

The `<VertFormat>` element is used to specify the required vertical formatting for an image, frame, or text component.

<a id="fal_elem_ref_sec_36_2"></a>
### Attributes:

- `type` specifies the required vertical formatting option.
  - For use in ImageryComponents and FrameComponents, this will be one of the values from the VerticalFormat enumeration.
  - For use in TextComponents, this will one of the values form the VerticalTextFormat enumeration.
- `component` Only for FrameComponent. Specifies the part of the frame that this formatting is to be used for. Should be "LeftEdge", "RightEdge" or "Background" from the FrameImageComponent enumeration. Optional attribute, defaults to "Background".

<a id="fal_elem_ref_sec_36_3"></a>
### Usage:

- The `<VertFormat>` element may only appear as a sub-element of the elements:
  - `<ImageryComponent>`
  - `<FrameComponent>`
  - `<TextComponent>`
- The `<VertFormat>` element may not contain any sub-elements.

<a id="fal_elem_ref_sec_36_4"></a>
### Examples:

This first example shows an ImageryComponent definition. We use `<VertFormat>` to specify that we want the image tiled to cover the entire width of the designated target area:

```xml
...
<ImageryComponent>
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="Width" ><AbsoluteDim value="25" /></Dim>
    <Dim type="Height" ><AbsoluteDim value="25" /></Dim>
  </Area>
  <Image imageset="myImageset" image="coolImage" />
  <VertFormat type="Tiled" />
  <HorzFormat type="Stretched" />
</ImageryComponent>
...
```

This second example is for a TextComponent. You can see `<VertFormat>` used here to specify that we want the text centred within the target area:

```xml
...
<TextComponent>
  <Area>
    <Dim type="LeftEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="TopEdge" ><AbsoluteDim value="0" /></Dim>
    <Dim type="RightEdge" ><UnifiedDim scale="1" type="Width" /></Dim>
    <Dim type="Height" ><UnifiedDim scale="1" type="Height" /></Dim>
  </Area>
  <VertFormat type="CentreAligned" />
</TextComponent>
...
```

<a id="fal_elem_ref_sec_37"></a>
## \<VertFormatProperty\> Element

<a id="fal_elem_ref_sec_37_1"></a>
### Purpose:

The `<VertFormatProperty>` element is intended to allow the system to access a property on the target window to obtain the vertical formatting to be used when drawing the component being defined.

<a id="fal_elem_ref_sec_37_2"></a>
### Attributes:

- `name`  specifies the name of the property to access. The named property must access a string value that will be set to one of the enumeration values appropriate for the component being defined (VerticalTextFormat for TextComponent, and VerticalFormat for FrameComponent and ImageryComponent).  Required attribute.
- `component`  Only for FrameComponent. Specifies the part of the frame that this formatting is to be used for. Should be "LeftEdge", "RightEdge" or "Background" from the FrameImageComponent enumeration. Optional attribute, defaults to "Background".

<a id="fal_elem_ref_sec_37_3"></a>
### Usage:

- The `<VertFormatProperty>` element may not contain sub-elements.
- The `<VertFormatProperty>` element may appear as a sub-element within any of the following elements:
  - `<ImageryComponent>` to specify a vertical formatting to be used the the image.
  - `<FrameComponent>` to specify a vertical formatting to be used for the frame background.
  - `<TextComponent>` to specify a vertical formatting to be used for the text.

<a id="fal_elem_ref_sec_37_4"></a>
### Examples:

<a id="fal_elem_ref_sec_38"></a>
## \<WidgetDim\> Element

<a id="fal_elem_ref_sec_38_1"></a>
### Purpose:

The `<WidgetDim>` element is used to define a component dimension for an area rectangle. `<WidgetDim>` is used to specify some dimension of an attached child widget for use as an area dimension.

<a id="fal_elem_ref_sec_38_2"></a>
### Attributes:

- `widget`  specifies a suffix which will be used when building the name of the widget to access. The final name of the child widget will be that of the parent with this suffix appended. If this is not specified, the target window itself is used. Optional attribute.
- `dimension`  specifies the widget dimension to be used. This should be set to one of the values defined in the DimensionType enumeration.  Required attribute.

<a id="fal_elem_ref_sec_38_3"></a>
### Usage:

- The `<WidgetDim>` element can appear as a sub-element in `<Dim>` to form a dimension specification for an area.
- The `<WidgetDim>` element can appear as a sub-element of `<OperatorDim>` to specify one of the operands for a dimension calculation.

<a id="fal_elem_ref_sec_38_4"></a>
### Examples:

This example shows using `<WidgetDim>` to obtain dimensions from an attached child widget '__auto_titlebar__', and also from the target window itself:

```xml
...
<Area>
  <Dim type="LeftEdge" >
    <AbsoluteDim value="0" />
  </Dim>
  <Dim type="TopEdge" >
    <WidgetDim widget="__auto_titlebar__" dimension="BottomEdge" />
  </Dim>
  <Dim type="Width" >
    <UnifiedDim scale="1" type="Width" />
  </Dim>
  <Dim type="BottomEdge" >
    <WidgetDim dimension="BottomEdge" />
  </Dim>
</Area>
...
```

<a id="fal_elem_ref_sec_39"></a>
## \<WidgetLook\> Element

<a id="fal_elem_ref_sec_39_1"></a>
### Purpose:

The `<WidgetLook>` element is the most important element within the system. It defines a complete widget 'look' which can be assigned to one of the Falagard base widget classes to create what is essentially a new widget type.

<a id="fal_elem_ref_sec_39_2"></a>
### Attributes:

- `name`  specifies the name of the WidgetLook being defined. If a WidgetLook with this name already exists within the system, it will be replaced with the new definition. Required attribute.

<a id="fal_elem_ref_sec_39_3"></a>
### Usage:

Note: the sub-elements should appear in the order that they are defined here.

- The `<WidgetLook>` element can contain the following sub-elements:
  - Any number of `<PropertyDefinition>` sub-elements defining new properties.
  - Any number of `<PropertyLinkDefinition>` sub-elements defining new linked properties.
  - Any number of `<Property>` sub-elements specifying default property values.
  - Any number of `<NamedArea>` sub-elements defining areas within the widget.
  - Any number of `<Child>` sub-elements defining component child widgets.
  - Any number of `<ImagerySection>` sub-elements defining imagery for the widget.
  - Any number of `<StateImagery>` sub-elements defining what to draw for widget states.
  - Any number of `<AnimationDefinition>` sub-elements defining animations for the WidgetLook. See: [Animation XML files.](https://static.cegui.org.uk/docs/0.8.7/xml_animation.html)
- The `<WidgetLook>` element may only appear as sub-elements of the root `<Falagard>` element.

<a id="fal_elem_ref_sec_39_4"></a>
### Examples:

The following example is the complete definition for 'TaharezLook/ListHeader'.  This is a trivial example that actually does no rendering, it just specifies a required property:

```xml
<WidgetLook name="TaharezLook/ListHeader">
  <Property
    name="SegmentWidgetType"
    value="TaharezLook/ListHeaderSegment"
  />
  <StateImagery name="Enabled" />
  <StateImagery name="Disabled" />
</WidgetLook>
```

---

Copyright (c) 2006 - 2011 Paul D Turner & The CEGUI Development Team

Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.2
or any later version published by the Free Software Foundation; with
no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
A copy of the license is included in [GNU-FDL-1.2.md](GNU-FDL-1.2.md).

*Modified version:* converted from the Doxygen sources of CEGUI 0.8.7 to Markdown.
Only formatting was changed; the text is the original.
