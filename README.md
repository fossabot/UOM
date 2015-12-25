# UOM
Unit of Measure conversion tool

The conversion factors and unit symbols are based on the Energistics UOM 1.0:
http://www.energistics.org/news/energistics-publishes-unit-of-measure-standard-v1-0
extended with few extra unit aliases and "unitless" special unit that cannot be converted.

The units are cases sensitives.

Please find few example of utilization:

 - Find conversion factors to be applied to convert from one unit to another

```
from uom import conversion_factors

scale, offset = conversion_factors(source="m", target="ft")
```
 - Convert a value from one unit to another

```
from uom import convert_value

print(convert(value=10, source="m", target="ft"))
```
 - Return the base (SI) unit and if you are using unit alias you can find the Energistics UOM symbol

```
from uom import base_unit, unit_alias

print(base_unit("kft.lbf"))
print(unit_alias("kft.lbf"))
```

If you have suggestions for improvement or you found bugs, please don't hesitate to put them in the issue list.
