from hashlib import new
import wrapper.libfptr10 as libfptr10

fptr = libfptr10.IFptr()
fptr.setSingleSetting(fptr.LIBFPTR_SETTING_MODEL, str(fptr.LIBFPTR_MODEL_ATOL_AUTO))
fptr.setSingleSetting(fptr.LIBFPTR_SETTING_PORT, str(fptr.LIBFPTR_PORT_USB));
fptr.open()

fptr.beep()

settings = fptr.getSettingsStr()

fptr.beginNonfiscalDocument()

fptr.setParam(fptr.LIBFPTR_PARAM_TEXT, settings)
fptr.printText()
fptr.setParam(fptr.LIBFPTR_PARAM_CUT_TYPE,fptr.LIBFPTR_CT_PART)

fptr.setParam(fptr.LIBFPTR_PARAM_BARCODE, settings)
fptr.setParam(fptr.LIBFPTR_PARAM_BARCODE_TYPE, fptr.LIBFPTR_BT_QR)
fptr.setParam(fptr.LIBFPTR_PARAM_SCALE, 5)
fptr.setParam(fptr.LIBFPTR_PARAM_ALIGNMENT,fptr.LIBFPTR_ALIGNMENT_CENTER)
fptr.printBarcode()

fptr.setParam(fptr.LIBFPTR_PARAM_PRINT_FOOTER,False)
fptr.endNonfiscalDocument()

fptr.close()