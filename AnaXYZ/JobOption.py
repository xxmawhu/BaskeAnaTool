Default = r'''// make by XYZData
#include "$ROOTIOROOT/share/jobOptions_ReadRec.txt"
#include "$MAGNETICFIELDROOT/share/MagneticField.txt"
#include "$RUNEVENTNUMBERALGROOT/share/jobOptions_RunEventNumber.txt"
#include "$ABSCORROOT/share/jobOptions_AbsCor.txt"
#include "$VERTEXFITROOT/share/jobOptions_VertexDbSvc.txt"
#include "$PI0ETATOGGRECALGROOT/share/jobOptions_Pi0EtaToGGRec.txt"
#include "$VEEVERTEXALGROOT/share/jobOptions_veeVertex.txt"
'''
tail = r'''
// Number of events to be processed (default is 10)
ApplicationMgr.EvtMax = -1;

// Set output level threshold (2=DEBUG, 3=INFO, 4=WARNING, 5=ERROR, 6=FATAL )
MessageSvc.OutputLevel = 5;
'''
