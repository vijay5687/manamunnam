from urllib.parse import quote

from pandas_profiling.report.presentation.core import HTML, Table, Sequence, Warnings


def get_dataset_overview(summary):
    dataset_info = Table(
        [
            
             {
                "name": "Total Number of Records",
                "value": summary["table"]["n"],
                "fmt": "fmt_numeric",
            },
            {
                "name": "Total Number of Columns",
                "value": summary["table"]["n_var"],
                "fmt": "fmt_numeric",
            },
            {
                "name": "Missing row cells",
                "value": summary["table"]["n_cells_missing"],
                "fmt": "fmt_numeric",
            },
            {
                "name": "Missing row cells (%)",
                "value": summary["table"]["p_cells_missing"],
                "fmt": "fmt_percent",
            },
            {
                "name": "Duplicate rows",
                "value": summary["table"]["n_duplicates"],
                "fmt": "fmt_numeric",
            },
            {
                "name": "Duplicate rows (%)",
                "value": summary["table"]["p_duplicates"],
                "fmt": "fmt_percent",
            },
          
        ],
        name="Table statistics",
    )

    dataset_types = Table(
        [
            {"name": type_name, "value": count, "fmt": "fmt_numeric"}
            for type_name, count in summary["table"]["types"].items()
        ],
        name="Variable types",
    )

    return Sequence(
        [dataset_info, dataset_types],
        anchor_id="dataset_overview",
        name="Overview",
        sequence_type="grid",
    )


def get_dataset_warnings(warnings, count):
    return Warnings(warnings=warnings, name=f"Analysis Summary ({count})", anchor_id="Analysis")



def get_dataset_reproduction(summary, date_start, date_end):
    version = summary["package"]["pandas_profiling_version"]
    config = quote(summary["package"]["pandas_profiling_config"])
    return Table(
        [
            {"name": "Analysis started", "value": date_start, "fmt": "fmt"},
            {"name": "Analysis finished", "value": date_end, "fmt": "fmt"},
            
        ],
        name="Run Statistics",
        anchor_id="run_statistics",
    )
