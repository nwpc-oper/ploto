# coding: utf-8
import json


def test_zonal_mean():
    print("test begin...")

    from ploto_server.common.esmdiag.metrics.mjo.figures.wavenum_freq_spectra import generate_figure_task

    task = generate_figure_task(
        figure_config={
            'name': 'wavenum_freq_spectra'
        },
        common_config={
            'model_info': {
                'id': "FGOALS-g3",
                'atm_id': "GAMIL",
                'ocn_id': "LICOM",
                'ice_id': "CICE",
            },
            'case_info': {
                'id': "gamil_wu_run11",
            },
            'date': {
                'start': "1979-01-01",
                'end': "1980-12-01"
            }
        }
    )

    print(json.dumps(task, indent=2))

    from ploto.run import run_ploto
    run_ploto(message={
        'data': task
    }, config={
        'base': {
            'run_base_dir': '/home/hujk/clusterfs/wangdp/ploto/run_base',
            'python_exe': '/home/hujk/.pyenv/versions/ploto-env/bin/python3'
        },
        'edp_fetcher': {
            'edp_module_path': "/home/hujk/pyProject/"
        },
        'esmdiag': {
            'root': '/home/hujk/ploto/ploto/vendor/esmdiag'
        }
    })


if __name__ == "__main__":
    test_zonal_mean()
