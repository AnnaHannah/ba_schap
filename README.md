# ba_schap

Das wird der praktische Teil von Annas Bachelorarbeit!


#### Probleme, die behoben werden können:

- Skiplist two direkt search implementieren
- aktuell funktionieren die Zeit messung mit dieser Funktion *time.perf_counter_ns()* 
es ist keine gute Funktion, da falls Windows Betriebssystem Prozesse für die jemweileigen Datenstruckturen erstellt, wird sleep von einem Prozess mit in die Time aufgenommen.
Das ist ungünstig, einer akternative wäre *time.time()* oder *time.time_ns*.
Das hat jedoch zurfolge dass Windows-Betriebssystem nicht genau mit diesem timer umgehen kann, angeblich weil das messintervall zu klein ist? ... also führt es zum wert *0*... das ist noch ungünstiger.
(Problem wird in Zukunft verschoben)
- Problem mit splaytree laufzeit, wenn ich den splay tree nutze wird er manipuliert, und das ist schlecht für laufzeit bei vielen Zahlen,  
