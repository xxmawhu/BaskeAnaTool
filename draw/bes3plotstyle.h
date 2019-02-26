/**********************************************************
 *                                                        *
 *         BES III Plotstyle: format functions            *
 *                                                        *
 *         August 2009, Niklaus Berger                    *
 *         nberger@ihep.ac.cn                             *
 *                                                        *
 *********************************************************/

#ifndef PLOTF__H
#define PLOTF__H

class TH1;
class TH1F;
class TAxis;
class TGraph;

// Format for data points
void FormatData(TH1 * datahist);
// Format for graph data points
void FormatData(TGraph * datagraph);
// Format Axis
void FormatAxis(TAxis *axis);
// Format for main MC (red line)
void FormatMC1(TH1 * mc1hist);
// Graph format for main MC (red line)
void FormatMC1(TGraph * mc1hist);
// Format for second MC or background
// (Blue shaded area)
void FormatMC2(TH1 * mc2hist);
// Graph Format for second MC or background
// (Blue line)
void FormatMC2(TGraph * mc2hist);
// Graph Format for third MC or background
// (Blue line)
void FormatMC3(TH1 * mc3hist);
void FormatMC3(TGraph * mc3hist);

void FormatMC4(TH1 * mc4hist);
void FormatMC4(TGraph * mc4hist);


// Name histogram axes
void NameAxes(TH1 * datahist, char * xname, char * yname);

// Write "BESIII" in the upper right corner
void WriteBes3();
// Write "Preliminary" below BESIII -
// to be used together with WriteBes3()
void WritePreliminary();

// Make a legend; 
// position will have to change depending on the data shape
void MakeLegend(TH1 * datahist,   // Histogram with data
		char * dataname,  // Description of data
		TH1 * mc1hist =0, // Histogram with first MC
		char * mc1name=0, // Description of first MC
		TH1 * mc2hist =0, // Histogram with 2nd MC/BG
		char * mc2name=0, // Description of second MC/BG
		double xlow = 0.55,      // Left edge of legend 
		                  //(fraction of canavas width)
		double ylow = 0.5,       // Bottom edge of legend
		                  //(fraction of canavas height)
		double xhi = 0.94,       // Right edge of legend 
		                  //(fraction of canavas width)
		double yhi = 0.7);       // Top edge of legend
		                  //(fraction of canavas height)

// Make a legend; 
// position will have to change depending on the data shape
void MakeLegend(TGraph * datahist,   // Graph with data
		char * dataname,  // Description of data
		TGraph * mc1hist =0, // Graph with first MC
		char * mc1name=0, // Description of first MC
		TGraph * mc2hist =0, // Graph with 2nd MC/BG
		char * mc2name=0, // Description of second MC/BG
		TGraph * mc3hist =0, // Graph with 3rd MC/BG
		char * mc3name=0, // Description of third MC/BG
		double xlow = 0.55,      // Left edge of legend 
		                  //(fraction of canavas width)
		double ylow = 0.5,       // Bottom edge of legend
		                  //(fraction of canavas height)
		double xhi = 0.94,       // Right edge of legend 
		                  //(fraction of canavas width)
		double yhi = 0.7);       // Top edge of legend
		                  //(fraction of canavas height)


// Make a legend (version for fit functions
// position will have to change depending on the data shape
void MakeLegend(TH1 * datahist,   // Histogram with data
		char * dataname,  // Description of data
		char ** functionnames, // list of function names
		double xlow = 0.55,      // Left edge of legend 
		                  //(fraction of canavas width)
		double ylow = 0.5,       // Bottom edge of legend
		                  //(fraction of canavas height)
		double xhi = 0.94,       // Right edge of legend 
		                  //(fraction of canavas width)
		double yhi = 0.7);       // Top edge of legend
		                  //(fraction of canavas height)

// Set the general style options
void SetStyle();

// Style options for "final" plots
// (no stat/fit box)
void SetPrelimStyle();

// Style options for internal meetings
// (stat/fit box)
void SetMeetingStyle();

// Plot a data MC plot
void PlotDataMC(char * filename,  // Name for the output files, 
		                  // without extension 
		TH1 * datahist,   // Histogram with data
		char * dataname,  // Description of data
		TH1 * mc1hist =0, // Histogram with first MC
		char * mc1name=0, // Description of first MC
		TH1 * mc2hist =0, // Histogram with 2nd MC/BG
		char * mc2name=0, // Description of second MC/BG
		int prelim = 1,    // Use 1 for Preliminary plot
		                   // 2 for a publication plot
                                   // and 0 for a meeting plot with 
		                   // stat and fit box
		double xlow = 0.55, // Left edge of legend 
		                    //(fraction of canavas width)
		double ylow = 0.5,  // Bottom edge of legend
		                    //(fraction of canavas height)
		double xhi = 0.94,  // Right edge of legend 
		                    //(fraction of canavas width)
		double yhi = 0.7);  // Top edge of legend
		                    //(fraction of canavas height)

// Plot data with one or more (fit) functions
// Functions should be part of the data histograms list of functions
// (i.e. perform fits with the "+" option or add other functions via
// datahist->GetListOfFunctions->Add(TF1 * function))
// functionnames should have at least as many elements as the function
// list
void PlotDataFit(char * filename,  // Name for the output files, 
		                  // without extension 
		TH1F * datahist,   // Histogram with data
		char * dataname,  // Description of data
		char ** functionnames,// Names of associated functions
		int prelim = 1,    // Use 1 for Preliminary plot
		                   // 2 for a publication plot
                                   // and 0 for a meeting plot with 
		                   // stat and fit box
		double xlow = 0.35, // Left edge of legend 
		                    //(fraction of canavas width)
		double ylow = 0.5,  // Bottom edge of legend
		                    //(fraction of canavas height)
		double xhi = 0.94,  // Right edge of legend 
		                    //(fraction of canavas width)
	        double yhi = 0.7);  // Top edge of legend
		                    //(fraction of canavas height)

// Scatter plot
void PlotScatter(char * filename,  // Name for the output files, 
		                   // without extension 
		 TH1 * datahist,   // Histogram with data
		 int prelim = 1    // Use 1 for Preliminary plot
		                   // 2 for a publication plot
                                   // and 0 for a meeting plot with 
		                   // stat and fit box
 );

#endif
