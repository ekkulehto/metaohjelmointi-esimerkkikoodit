;; ilman makroa luetaan sisältä ulospäin
;; tulostaa: Ilman makroa: 5
(println (str "Ilman makroa: "(inc (* 2 2))))

;; threading macrolla (->>) luetaan vasemmalta oikealle
;; saatu arvo asetetaan aina seuraavan funktion viimeiseksi argumentiksi
(->> 2
    (* 2)                       ; => (* 2 2) => 4
    (inc)                       ; => (inc 4) => 5
    (str "Makron kanssa: ")     ; => (str "Makron kanssa: " 5)
    (println))                  ; => (println "Makron kanssa: 5")
                                ; tulostaa: Makron kanssa: 5

;; parantaa luettavuutta monimutkaisessa datan käsittelyssä