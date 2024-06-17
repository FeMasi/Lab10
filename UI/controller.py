import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._currentCountry =None

    def handleRaggiungibili(self):
        pass
    def handleCalcola(self, e):
        anno = self._view._txtAnno.value
        try:
            yearN = int(anno)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Please provide a numerical value in field. "))
            self._view.update_page()
            return
        if yearN>2016 or yearN<1816:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text("Inserire un anno compreso tra il 1816 e il 2016"))
            self._view.update_page()
            return

        self._model.buildGraph(yearN)

        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))
        self._view._txt_result.controls.append(
            ft.Text(f"Il grafo ha {self._model.getNumCompConnesse()} componenti connesse."))
        self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))

        for n in self._model.getNodes():
            self._view._txt_result.controls.append(
                ft.Text(f"{n} -- {self._model.getNumConfinanti(n)} vicini."))

        self._view._ddStato.disabled = False
        self._view._btnRaggiungibili.disabled = False

        self._fillDD()
        self._view.update_page()

    def _fillDD(self):
        allStati = self._model.getNodes()

        for s in allStati:
            self._view._ddStato.options.append(ft.dropdown.Option(text=s.StateNme,
                                                 data=s,
                                                 on_click=self.read_DD_Stato))

    def read_DD_Stato(self, e):
        print("read_DD_Stato called ")
        if e.control.data is None:
            self._currentCountry = None
        else:
            self._currentCountry = e.control.data

        print(self._currentCountry)

