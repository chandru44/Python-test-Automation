from datetime import datetime, timedelta
import xml.etree.ElementTree as ET

xml_file = "test_payload1.xml"
new_xml_file = "test_payload_new.xml"


def update(x, y):
    depart_date = datetime.now() + timedelta(days=x)
    return_date = datetime.now() + timedelta(days=y)

    if return_date <= depart_date:
        print("Invalid return date")


    root = ET.parse(xml_file)
    root.find("./REQUEST/TP/DEPART").text = depart_date.strftime("%Y%m%d")
    root.find("./REQUEST/TP/RETURN").text = return_date.strftime("%Y%m%d")
    root.write(new_xml_file)


if __name__ == '__main__':
    update(10, 20)