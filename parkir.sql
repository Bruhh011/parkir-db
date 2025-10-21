--
-- PostgreSQL database dump
--

\restrict 8yoAGdFImKyXevXIN8bSZQ6zhy5gZq4GqvELwfsw3i54TJCkSHzfQ2LpBOvc1IQ

-- Dumped from database version 17.6
-- Dumped by pg_dump version 17.6

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: absensi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.absensi (
    id_petugas integer,
    tanggal_absen timestamp with time zone,
    kehadiran character varying(255)
);


ALTER TABLE public.absensi OWNER TO postgres;

--
-- Name: insiden; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.insiden (
    id_rekaman integer NOT NULL,
    keterangan character varying(255),
    no_struk integer
);


ALTER TABLE public.insiden OWNER TO postgres;

--
-- Name: jabatan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jabatan (
    id_jabatan integer NOT NULL,
    nama_jabatan character varying(255),
    hak_akses text,
    gaji_pokok double precision
);


ALTER TABLE public.jabatan OWNER TO postgres;

--
-- Name: jadwal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.jadwal (
    no_struk integer NOT NULL,
    tanggal timestamp with time zone,
    jam_masuk character varying(255),
    jam_keluar character varying(255),
    id_petugas integer,
    plat_nomor character varying(255),
    bayar character varying(255),
    no_pintu integer,
    no_tempat integer
);


ALTER TABLE public.jadwal OWNER TO postgres;

--
-- Name: kendaraan; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.kendaraan (
    plat_nomor character varying(255) NOT NULL,
    jenis_kendaraan text
);


ALTER TABLE public.kendaraan OWNER TO postgres;

--
-- Name: lokasi; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lokasi (
    lantai integer,
    no_tempat integer NOT NULL,
    ketersediaan character varying(255)
);


ALTER TABLE public.lokasi OWNER TO postgres;

--
-- Name: menjabat; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.menjabat (
    id_petugas integer,
    id_jabatan integer
);


ALTER TABLE public.menjabat OWNER TO postgres;

--
-- Name: petugas; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.petugas (
    id_petugas integer NOT NULL,
    nama_petugas character varying(255)
);


ALTER TABLE public.petugas OWNER TO postgres;

--
-- Name: pintu; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.pintu (
    no_pintu integer NOT NULL,
    jenis_pintu character varying(255),
    no_tempat integer
);


ALTER TABLE public.pintu OWNER TO postgres;

--
-- Data for Name: absensi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.absensi (id_petugas, tanggal_absen, kehadiran) FROM stdin;
\.


--
-- Data for Name: insiden; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.insiden (id_rekaman, keterangan, no_struk) FROM stdin;
\.


--
-- Data for Name: jabatan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jabatan (id_jabatan, nama_jabatan, hak_akses, gaji_pokok) FROM stdin;
\.


--
-- Data for Name: jadwal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.jadwal (no_struk, tanggal, jam_masuk, jam_keluar, id_petugas, plat_nomor, bayar, no_pintu, no_tempat) FROM stdin;
\.


--
-- Data for Name: kendaraan; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.kendaraan (plat_nomor, jenis_kendaraan) FROM stdin;
\.


--
-- Data for Name: lokasi; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lokasi (lantai, no_tempat, ketersediaan) FROM stdin;
\.


--
-- Data for Name: menjabat; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.menjabat (id_petugas, id_jabatan) FROM stdin;
\.


--
-- Data for Name: petugas; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.petugas (id_petugas, nama_petugas) FROM stdin;
\.


--
-- Data for Name: pintu; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.pintu (no_pintu, jenis_pintu, no_tempat) FROM stdin;
\.


--
-- Name: insiden insiden_ID_Rekaman; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insiden
    ADD CONSTRAINT "insiden_ID_Rekaman" PRIMARY KEY (id_rekaman);


--
-- Name: jabatan jabatan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jabatan
    ADD CONSTRAINT jabatan_pkey PRIMARY KEY (id_jabatan);


--
-- Name: jadwal jadwal_NO_struk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal
    ADD CONSTRAINT "jadwal_NO_struk" PRIMARY KEY (no_struk);


--
-- Name: kendaraan kendaraan_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.kendaraan
    ADD CONSTRAINT kendaraan_pkey PRIMARY KEY (plat_nomor);


--
-- Name: lokasi lokasi_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lokasi
    ADD CONSTRAINT lokasi_pkey PRIMARY KEY (no_tempat);


--
-- Name: petugas petugas_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.petugas
    ADD CONSTRAINT petugas_pkey PRIMARY KEY (id_petugas);


--
-- Name: pintu pintu_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pintu
    ADD CONSTRAINT pintu_pkey PRIMARY KEY (no_pintu);


--
-- Name: absensi absensi_id_petugas; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.absensi
    ADD CONSTRAINT absensi_id_petugas FOREIGN KEY (id_petugas) REFERENCES public.petugas(id_petugas) NOT VALID;


--
-- Name: CONSTRAINT absensi_id_petugas ON absensi; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON CONSTRAINT absensi_id_petugas ON public.absensi IS 'FK id_petugas';


--
-- Name: jadwal id_petugas_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal
    ADD CONSTRAINT id_petugas_fkey FOREIGN KEY (id_petugas) REFERENCES public.petugas(id_petugas);


--
-- Name: insiden insiden_NO_struk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insiden
    ADD CONSTRAINT "insiden_NO_struk" FOREIGN KEY (no_struk) REFERENCES public.jadwal(no_struk) NOT VALID;


--
-- Name: jadwal jadwal_no_pintu; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal
    ADD CONSTRAINT jadwal_no_pintu FOREIGN KEY (no_pintu) REFERENCES public.pintu(no_pintu) NOT VALID;


--
-- Name: jadwal jadwal_no_tempat; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal
    ADD CONSTRAINT jadwal_no_tempat FOREIGN KEY (no_tempat) REFERENCES public.lokasi(no_tempat) NOT VALID;


--
-- Name: jadwal jadwal_plat_nomer; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.jadwal
    ADD CONSTRAINT jadwal_plat_nomer FOREIGN KEY (plat_nomor) REFERENCES public.kendaraan(plat_nomor) NOT VALID;


--
-- Name: menjabat menjabat_id_jabatan; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.menjabat
    ADD CONSTRAINT menjabat_id_jabatan FOREIGN KEY (id_jabatan) REFERENCES public.jabatan(id_jabatan) NOT VALID;


--
-- Name: menjabat menjabat_id_petugas; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.menjabat
    ADD CONSTRAINT menjabat_id_petugas FOREIGN KEY (id_petugas) REFERENCES public.petugas(id_petugas) NOT VALID;


--
-- Name: pintu pintu_no_tempat; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.pintu
    ADD CONSTRAINT pintu_no_tempat FOREIGN KEY (no_tempat) REFERENCES public.lokasi(no_tempat) NOT VALID;


--
-- PostgreSQL database dump complete
--

\unrestrict 8yoAGdFImKyXevXIN8bSZQ6zhy5gZq4GqvELwfsw3i54TJCkSHzfQ2LpBOvc1IQ

